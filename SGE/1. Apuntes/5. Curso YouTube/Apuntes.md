# Índice

- Herencia Python
- Herencia en vistas XML
- Campo calculado
- Decoradores

# Teoría

> [!NOTE]
> Para iniciar un proyecto necesitas:
> - Una nueva carpeta guardada en "extra-addons"
> - `__init__.py`
> - `__manifest__.py
> - Carpeta `models`
> 	- `__init__.py`
> - Carpeta `views`
> 	- `__init__.py`


> [!NOTE]
Cada directorio donde alojes código en python, necesitas un archivo `__init__.py`.


# manifest.py

> Es el archivo donde se añade la descripción, nombre del módulo, herencias/dependencias, vistas y configuración


Cuando creamos una clase, estamos creando una tabla en postgresql

```python
# Importamos librerías
from odoo import models, fields, api

# Creamos clase
class Student(models.Model)
# Queremos que tenga dos campos
# Tenemos que indicarle que tipo de dato (lo hacemos con fields.)
	name = fields.Char
# Si queremos que tenga un nombre dicho campo en la interfaz:
	name = fields.Char(string="Nombre campo", required=True)
	age = fields.Integer(string="Edad")
```

### **Herencia**:

• Las clases heredan de una de las superclases de Odoo:
	• `Model`: Para modelos persistentes (con base de datos).
	• `TransientModel`: Para modelos temporales, limpiados periódicamente.
	• `AbstractModel`: Para clases abstractas que no crean tablas en la base de datos.


Para que estos modelos (clases) se puedan ver de forma gráfica, tienes que añadirlos en las vistas (carpeta view).

# Views

La estructura mínima de una vista
```xml
<odoo>
	<data>

	</data>
</odoo>
```

Las interfaces ya están creadas, solo hay que llamarlas. Como por ejemplo, una lista, un formulario..

```xml
<odoo>
	<data>
		<record id="" model="ir.ui.view">
		</record>
	</data>
</odoo>
```

``` xml
# Inicio de una vista
<record model="ir.ui.view" id="view_id">
# metadatos
  <field name="name">Nom_de_la_vista</field>
  <field name="model">Objecte_al_que_fa_referència</field>
  <field name="arch" type="xml">
   	<!-- Aquí va el contingut específic de la vista->
    <VIEW_TYPE>
      <VIEW_SPECIFICATIONS/>
    </VIEW_TYPE>
  	<!-- Fi del contingut específic de la vista->
  </field>
</record>
```