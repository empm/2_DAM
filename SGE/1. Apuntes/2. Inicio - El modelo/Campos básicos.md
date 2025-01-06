> El módulo **ORM (Object Relational Mapping)** en Odoo permite interactuar con bases de datos de manera eficiente y estructurada, gestionando modelos, campos y operaciones de datos. Su diseño facilita la creación y personalización de módulos en Odoo mediante una abstracción de la base de datos.

  
# **Características clave del ORM**

1. **Estructura jerárquica**: Relaciona modelos y dependencias entre ellos.
2. **Consistencia y validación**: Garantiza restricciones y datos válidos.
3. **Metadatos dependientes del estado**: Ajusta la información según el contexto del objeto.
4. **Consultas optimizadas**: Procesamiento eficiente de acciones múltiples.
5. **Valores predeterminados**: Define configuraciones iniciales para los campos.
6. **Permisos optimizados**: Gestión granular de accesos.
7. **Persistencia**: Datos almacenados en PostgreSQL.
8. **Conversión de datos**: Facilita el manejo entre tipos de datos.
9. **Sistema de caché multinivel**: Mejora el rendimiento.
10. **Herencia múltiple**: Soporta composición e inyección de funcionalidades.

# **Tipos de modelos en Odoo**

1. **Model**: Base para modelos persistentes en la base de datos.
2. **TransientModel**: Modelos temporales, limpiados periódicamente.
3. **AbstractModel**: Superclases abstractas para compartir lógica entre modelos.
  

# **Campos principales en modelos de Odoo**


Los campos en Odoo son definidos como atributos dentro de los modelos. Se agrupan en tres tipos principales:

1. **Campos clásicos**:
	• **Char**: Cadenas de texto.
	• **Integer**: Números enteros.
	• **Float**: Números decimales.
	• **Boolean**: Valores de verdadero/falso.
	• **Text**: Cadenas largas.

2. **Campos relacionales**:
	• **Many2one**: Relación con un registro único de otro modelo.
	• **One2many**: Relación con múltiples registros en otro modelo.
	• **Many2many**: Relación bidireccional entre múltiples registros.

3. **Campos funcionales**:
	• Calculados dinámicamente mediante funciones (por ejemplo, sumas, promedios).

  
# **Atributos principales en campos**

1. **string**: Etiqueta visible para el usuario.
2. **default**: Valor predeterminado (estático o calculado).
3. **required**: Campo obligatorio.
4. **readonly**: Solo lectura.
5. **index**: Si se indexa en la base de datos.
6. **compute**: Método para calcular valores dinámicamente.
7. **help**: Descripción o ayuda para el usuario.
8. **groups**: Restricción de acceso según grupos de usuarios.


# **Atributos clave del modelo**

1. **_name**: Nombre del modelo en notación de puntos (e.g., module.model_name).
2. **_inherit**: Define herencia de otro modelo.
3. **_description**: Nombre informal del modelo.
4. **_sql_constraints**: Restricciones SQL personalizadas.
5. **_order**: Campo predeterminado para ordenar resultados (e.g., id).
6. **_rec_name**: Campo para etiquetar registros (por defecto, name).
7. **_parent_name**: Relación jerárquica en un modelo.
8. **_auto**: Si el modelo genera una tabla SQL (por defecto, True).


# **Funcionalidades básicas que ofrece el ORM**

• **Operaciones CRUD**:
	• Crear, leer, actualizar y eliminar registros.

• **Herencia**:
	• Dos mecanismos: clásica (extiende funcionalidad) y composición (exposición de campos de otros modelos).

• **Control de accesos**:
	• Gestión avanzada de permisos por grupos y usuarios.

• **Optimización del rendimiento**:
	• Uso de caché y consultas optimizadas.

• **Gestión de relaciones**:
	• Manipulación y acceso eficiente a relaciones complejas entre modelos.

  
# **Campos principales en los modelos**

**Campo** **Descripción**
**Char** Texto corto (cadenas).
**Integer** Números enteros.
**Float** Decimales con precisión configurable.
**Many2one** Relación hacia un único registro de otro modelo.
**One2many** Relación hacia múltiples registros de otro modelo.
**Many2many** Relación entre múltiples registros.
**Date/Datetime** Manejo de fechas y horas.
**Binary** Archivos binarios como imágenes o documentos.