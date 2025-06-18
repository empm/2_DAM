from odoo import models, fields, api, _
from dateutil.relativedelta import relativedelta
from datetime import date

class Estudiante(models.Model):
    _name = 'academia.estudiante'  # Nombre técnico del modelo
    _description = 'Estudiante'    # Descripción legible
    _order = 'apellido asc, nombre asc'  # Ordenación por defecto
    _sql_constraints = [
        ('dni_unique', 'unique(dni)', 'El DNI debe ser único.')  # Restricción SQL para campo único
    ]

    nombre = fields.Char(string='Nombre', required=True)  # Campo texto obligatorio
    apellido = fields.Char(string='Apellido', required=True)  # Campo texto obligatorio
    dni = fields.Char(string='DNI', required=True)  # Campo texto obligatorio, único por restricción
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')  # Campo fecha
    edad = fields.Integer(
        string='Edad',
        compute='_compute_edad',  # Campo calculado con método
        store=True,
        readonly=True  # No editable por usuario
    )

    nota_examen = fields.Float(
        string='Nota examen',
        digits=(3, 2),  # Precisión: máximo 3 dígitos, 2 decimales
    )
    aprobado = fields.Boolean(
        string='Aprobado',
        compute='_compute_aprobado',  # Campo calculado según nota
        store=True
    )

    estado = fields.Selection(
        [('nuevo', 'Nuevo'), ('activo', 'Activo'), ('inactivo', 'Inactivo')],
        string='Estado',
        default='nuevo',  # Valor por defecto
        required=True,
        readonly=False,
        help='Estado actual del estudiante'  # Descripción para usuario
    )

    pais_usuario = fields.Many2one(
        'res.country',  # Relación a modelo país
        string='País del usuario',
        default=lambda self: self.env.user.partner_id.country_id.id  # País por defecto según usuario actual
    )

    curso_ids = fields.Many2many(
        'academia.curso',  # Relación muchos a muchos con cursos
        string='Cursos'
    )

    calificaciones_ids = fields.One2many(
        'academia.calificacion',  # Relación uno a muchos con calificaciones
        'estudiante_id',  # Campo inverso en calificación
        string='Calificaciones Detalladas'
    )

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        """Calcula la edad a partir de la fecha de nacimiento usando relativedelta."""
        for record in self:
            if record.fecha_nacimiento:
                hoy = date.today()
                diferencia = relativedelta(hoy, record.fecha_nacimiento)
                record.edad = diferencia.years
            else:
                record.edad = 0

    @api.depends('nota_examen')
    def _compute_aprobado(self):
        """Determina si está aprobado según la nota de examen (>=5)."""
        for record in self:
            record.aprobado = record.nota_examen >= 5.0

    def name_get(self):
        """Concatena nombre y apellido para mostrar el nombre completo."""
        result = []
        for record in self:
            nombre_completo = f"{record.nombre or ''} {record.apellido or ''}".strip()
            result.append((record.id, nombre_completo))
        return result

    def estado_estudiante(self):
        """Ejemplo de función que imprime si está aprobado o suspendido."""
        for record in self:
            if record.aprobado:
                print(f"El estudiante {record.nombre} está aprobado.")
            else:
                print(f"El estudiante {record.nombre} está suspendido.")

class Curso(models.Model):
    _name = 'academia.curso'  # Modelo para cursos
    _description = 'Curso'

    nombre = fields.Char(string='Nombre del curso', required=True)  # Nombre obligatorio
    descripcion = fields.Text(string='Descripción')  # Descripción opcional

    estudiante_ids = fields.Many2many(
        'academia.estudiante',  # Relación inversa muchos a muchos con estudiantes
        string='Estudiantes',
        relation='estudiante_curso_rel',  # Tabla relacional en BD
        column1='curso_id',
        column2='estudiante_id'
    )

class Calificacion(models.Model):
    _name = 'academia.calificacion'  # Modelo para calificaciones detalladas
    _description = 'Calificación Detallada'

    nota = fields.Float(
        string='Nota',
        required=True,
        digits=(3, 2)  # Precisión decimal para la nota
    )
    comentario = fields.Text(string='Comentario')  # Comentario libre
    estudiante_id = fields.Many2one(
        'academia.estudiante',  # Relación a estudiante
        string='Estudiante',
        required=True
    )

class ResPartner(models.Model):
    _inherit = 'res.partner'  # Extiende el modelo existente res.partner

    codigo_estudiante = fields.Char(string='Código de Estudiante')  # Nuevo campo código
