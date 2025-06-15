**Banco de Preguntas y Respuestas – Odoo 13**

---

**1. ¿Cómo se define una relación Many2one en Odoo?**

Una relación Many2one en Odoo se define usando el campo `fields.Many2one` en el modelo. Este tipo de relación indica que muchos registros del modelo actual pueden estar relacionados con un único registro de otro modelo.

Ejemplo:

```python
class Libro(models.Model):
    _name = 'biblioteca.libro'
    autor_id = fields.Many2one('biblioteca.autor', string='Autor')
```

---

**2. ¿Qué significa heredar una vista con **``**?**

Heredar una vista con `mode="primary"` indica que la vista hija actuará como base para ese modelo, sustituyendo a la principal si existe. Es útil cuando se extiende un modelo mediante herencia delegada (`_inherits`) y se quiere que las vistas usen el modelo hijo como principal.

```xml
<record id="mi_vista" model="ir.ui.view">
  <field name="inherit_id" ref="otra_vista.form"/>
  <field name="mode">primary</field>
</record>
```

---

**3. ¿Qué pasa si se elimina un registro relacionado?**

Dependerá del atributo `ondelete` en la relación:

- `ondelete='cascade'`: se eliminarán los registros hijos automáticamente.
- `ondelete='set null'`: se pondrá el campo a `null`.
- `ondelete='restrict'`: impide la eliminación si hay relaciones.

Ejemplo:

```python
fields.Many2one('res.partner', string='Cliente', ondelete='restrict')
```

---

**4. ¿Qué es una relación Many2many y cómo se utiliza?**

Permite la relación de muchos registros con muchos otros registros. Se usa `fields.Many2many` y puede especificar el nombre de la tabla relacional (`relation`) y los campos de relación.

Ejemplo:

```python
alumnos = fields.Many2many('school.alumno', string='Alumnos')
```

---

**5. ¿Para qué sirve el campo **``** en una vista?**

Sirve para indicar que la vista está heredando otra vista existente. Se usa para modificar su estructura con instrucciones `xpath`, `field`, etc.

Ejemplo:

```xml
<record id="vista_extendida" model="ir.ui.view">
  <field name="inherit_id" ref="modulo.vista_original"/>
  <field name="arch" type="xml">
    <xpath expr="//field[@name='name']" position="after">
      <field name="nuevo_campo"/>
    </xpath>
  </field>
</record>
```

