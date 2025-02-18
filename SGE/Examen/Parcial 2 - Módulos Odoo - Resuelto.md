> Realizar las clases para ODOO13 en el framework de OpenObject cumpliendo los estándares indicados durante el curso.

> El modulo se llamará de la siguiente forma: apellido1 del alumno y las Clases de OpenObject apellido1.clase. El modulo esta basado en el boceto dibujado.

> Como mínimo cada clase en python deberá de tener al menos 7 campos.

# 1) Código python de la clase bomberocamion

Esta clase representa la relación **Muchos a Muchos** entre **Bomberos** y **Camiones**, ya que un bombero puede estar asignado a varios camiones en diferentes momentos y un camión puede tener varios bomberos asignados.

> No incluir required o store si no lo pide

---

## Código en Python para `bomberocamion`

```python
from odoo import models, fields

class BomberoCamion(models.Model):
    _name = 'apellido1.bomberocamion'
    _description = 'Relación entre Bomberos y Camiones'

    bombero_id = fields.Many2one('apellido1.bombero', string="Bombero")
    camion_id = fields.Many2one('apellido1.camion', string="Camión")
    fecha_inicio = fields.Date('Fecha de Inicio')
    fecha_fin = fields.Date('Fecha de Fin')

    puesto = fields.Char(related = "bombero_id.puesto")

    descripcion = fields.Text('Descripción de la Asignación')
    nombre_bombero = fields.Char(related='bombero_id.name', string="Nombre del bombero")
```

---

### **Explicación del Código**

1. **Nombre y descripción del modelo**

```python
_name = 'apellido1.bomberocamion'
_description = 'Relación entre Bomberos y Camiones'
```

- `_name`: Define el identificador del modelo dentro del módulo `apellido1`.
- `_description`: Es una breve descripción del propósito de la clase.

2. **Relaciones con `Bombero` y `Camión`**

```python
bombero_id = fields.Many2one('apellido1.bombero', string="Bombero")
camion_id = fields.Many2one('apellido1.camion', string="Camión")
```

-  **`Many2one`** conecta un `bomberocamion` con un **bombero** y un **camión**.

3. **Campos de Fechas para el Tiempo de Asignación**

```python
fecha_inicio = fields.Date('Fecha de Inicio')
fecha_fin = fields.Date('Fecha de Fin')
```

- `fecha_inicio`: Registra cuándo el bombero comenzó a estar asignado al camión.
- `fecha_fin`: Se deja opcional, en caso de que el bombero siga en el camión.

4. **Cambio de `Selection` a `Related Field` para el Puesto del Bombero**

```python
puesto_bombero = fields.Char(related="bombero_id.puesto", string="Puesto")
```

- En lugar de definir un campo `Selection` estático en `bomberocamion`, podemos **heredar el puesto del bombero vinculado (`bombero_id.puesto`)** usando un campo `related`.
- Ahora `puesto_bombero` obtiene automáticamente el valor de `bombero_id.puesto`.

5. **Descripción de la Asignación**

```python
descripcion = fields.Text('Descripción de la Asignación')
```

- Campo de texto libre donde se puede anotar información adicional.


# 2) Clase bombero, en la cual debemos tener al menos cinco de los campos de tipos diferentes:

En este ejercicio se nos pide crear la clase `Bombero` con las siguientes características:

1. **DNI único y obligatorio**
2. **Fecha de nacimiento (`Date`)**
3. **Campo de selección para el puesto** (conductor, copiloto, capitán, bombero raso)
4. **Puesto por defecto: bombero raso**
5. **Ordenar por `apellido1`**
6. **Ver los camiones en los que ha estado asignado**

---

## Código en Python para `Bombero`

```python
from odoo import models, fields

class Bombero(models.Model):
    _name = 'apellido1.bombero'
    _description = 'Bombero'
    _order = 'apellido1'

    name = fields.Char('Nombre')
    apellido1 = fields.Char('Primer Apellido')
    apellido2 = fields.Char('Segundo Apellido')
    dni = fields.Char('DNI')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')

    puesto = fields.Selection([
        ('conductor', 'Conductor'),
        ('copiloto', 'Copiloto'),
        ('capitan', 'Capitán'),
        ('bomberoRaso', 'Bombero Raso')
    ], string="Puesto", default='bomberoRaso')

    bomberocamion_ids = fields.One2many('apellido1.bomberocamion', 'bombero_id', string="Historial de Camiones")

    _sql_constraints = [('dni_unique', 'UNIQUE(dni)', 'El DNI debe ser único.')]
```

---

### **Explicación del Código**

1. **Nombre del modelo y ordenación**

```python
_name = 'apellido1.bombero'
_description = 'Bombero'
_order = 'apellido1'
```

- `_name`: Identifica el modelo dentro del módulo `apellido1`.
- `_description`: Breve descripción del modelo.
- `_order = 'apellido1'`: Ordena los registros por `apellido1` en vistas tipo lista.

2. **Campos Básicos**

```python
name = fields.Char('Nombre')
apellido1 = fields.Char('Primer Apellido')
apellido2 = fields.Char('Segundo Apellido')
```

- `name`: Nombre del bombero.
- `apellido1`: Primer apellido (obligatorio)
- `apellido2`: Segundo apellido (opcional).

3. **Campo `dni` (Único y Obligatorio)**

```python
dni = fields.Char('DNI')
```

- **⚠️ Odoo no admite `unique=True` en `fields.Char`.** En su lugar, se debe usar **`_sql_constraints`**, que impone la restricción directamente en la base de datos.

4. **Fecha de Nacimiento**

```python
fecha_nacimiento = fields.Date('Fecha de Nacimiento', required=True)
```

- Permite almacenar la fecha de nacimiento del bombero.

5. **Campo de Selección para el Puesto**

```python
puesto = fields.Selection([
    ('conductor', 'Conductor'),
    ('copiloto', 'Copiloto'),
    ('capitan', 'Capitán'),
    ('bomberoRaso', 'Bombero Raso')
], string="Puesto", default='bomberoRaso')
```

- Opciones predefinidas para el puesto del bombero.
- Por defecto es **"Bombero Raso"**.

6. **Historial de Camiones (Relación `One2many`)**

```python
bomberocamion_ids = fields.One2many('apellido1.bomberocamion', 'bombero_id', string="Historial de Camiones")
```

- Permite ver en **qué camiones ha estado asignado** este bombero.

7. **Restricción de Unicidad para `DNI`**

```python
_sql_constraints = [('dni_unique', 'UNIQUE(dni)', 'El DNI debe ser único.')]
```

- dni_unique → Es un nombre identificador para la restricción (debe ser único en el módulo).
- UNIQUE(dni) → Impone una restricción de unicidad en la base de datos.
- 'El DNI debe ser único.' → Mensaje de error si se intenta duplicar un dni.


# 3) Vista de calendar de la clase bomberocamion.

Se nos pide crear una vista de calendario para la clase `bomberocamion`, donde se marque el evento que simboliza **el tiempo que un bombero está asignado a un camión**.

📌 **Requisitos clave:**
1. **Debe mostrar los eventos basados en `fecha_inicio` y `fecha_fin`.**
2. **Al hacer clic en un evento, debe mostrar el bombero y el camión.**

---

## **Código XML para la Vista Calendar de `bomberocamion`**

```xml
<record model="ir.ui.view" id="apellido1.bomberocamion_calendar">
    <field name="name">Calendario de Bomberos en Camiones</field>
    <field name="model">apellido1.bomberocamion</field>
    <field name="arch" type="xml">
        <calendar string="Asignaciones de Bomberos"
                  date_start="fecha_inicio"
                  date_stop="fecha_fin"
                  color="puesto">
            <field name="bombero_id"/>
            <field name="camion_id"/>
            <field name="puesto"/>
        </calendar>
    </field>
</record>
```

---

### **Explicación del Código**

1. **Definimos la vista en `ir.ui.view`**

    ```xml
    <record model="ir.ui.view" id="view_bomberocamion_calendar">
    ```

- Creamos una vista nueva para el modelo `apellido1.bomberocamion`.
2. **Campos clave de la vista `calendar`**

    ```xml
    <calendar string="Asignaciones de Bomberos"
              date_start="fecha_inicio"
              date_stop="fecha_fin"
              color="puesto">
    ```

- **`date_start="fecha_inicio"`** → Marca el inicio de la asignación.
- **`date_stop="fecha_fin"`** → Muestra la duración hasta `fecha_fin`.
- **`color="puesto"`** → Diferencia visualmente los eventos según el puesto del bombero.

3. **Campos que se mostrarán en cada evento**
   
    ```xml
    <field name="bombero_id"/>
    <field name="camion_id"/>
    <field name="puesto"/>
    ```

- `bombero_id`: Indica qué bombero está asignado.
- `camion_id`: Muestra el camión en el que está asignado.
- `puesto`: Diferencia visualmente a los bomberos según su rol.


# 4) En vista de calendar de la clase bomberocamion, deseamos que se muestre: 

📌 **Requisito:**  
En la vista **calendar de `bomberocamion`**, en lugar de mostrar los IDs de `bombero_id` y `camion_id`, se debe mostrar **el nombre del bombero concatenado con el nombre del camión**.

---

## **Solución: crear una función`**

Para lograr esto, ahora hemos implementado la función **`name_get`**, que define cómo se mostrará el nombre del registro en Odoo.

```python
from odoo import models, fields, api

class BomberoCamion(models.Model):
	...

def name_get(self):
    result = []
    for record in self:
        name = f" {record.bombero_id.name} - {record.camión_id.name}"
		result.append((record.id, name))
    return result
```

### **Explicación del Código**

1. **Definición de `name_get`**

```python
def name_get(self):
```

- Esta función **personaliza cómo se muestra un registro en Odoo**, especialmente en listas y vistas de selección.

2. **Recorremos los registros en `self`**

```python
result = []
for record in self:
```

- Odoo puede llamar esta función con **varios registros**, por lo que usamos un `for` para recorrerlos.

3. **Concatenamos el nombre del Bombero y el Camión**

```python
name = f"{record.bombero_id.name} - {record.camion_id.name}"
```

- Se crea un **nombre legible** combinando el nombre del **bombero** y el **camión**.

4. **Guardamos la información en `result`**

```python
result.append((record.id, name))
```

- Odoo **requiere que `name_get` devuelva una lista de tuplas** en el formato: `(ID del registro, Nombre a mostrar)`.
- Esto permite que en las vistas y selecciones en Odoo, en lugar de ver `"BomberoCamion(3)"`, se vea:  **"Juan Pérez - Camión Alfa"**.

5. **Retornamos `result`**

```python
return result
```

- Odoo usará estos nombres en vistas tipo `tree`, `form`, `calendar`, etc.

---

### **¿Qué Cambia con `name_get`?**

✅ **Antes**, en la vista Calendar se mostraban los IDs del bombero y camión.  
✅ **Ahora**, se muestra `"Nombre del Bombero - Nombre del Camión"` en todas las vistas donde se usa este modelo.  
✅ **Se evita la necesidad de un campo adicional**, ya que la función `name_get` personaliza cómo se visualizan los registros en Odoo.
📌 **Con esta modificación, cuando un usuario seleccione un registro de `bomberocamion`, verá algo comprensible en vez de un número de ID.** 🚀
✔ **La vista `calendar` ya no necesita un campo adicional para mostrar el nombre completo, porque `name_get` se encarga de ello.**


# 5) Vista de formulario de clase bombero, de tal forma que se añadan cuantos más elementos de xml mejor (por ejemplo: notebook, y separator, att...)

📌 **Requisitos del ejercicio:**

1. **Agregar un campo booleano** para indicar si el bombero tiene carnet de camión.
2. **Si tiene carnet**, mostrar un campo para ingresar el **número de carnet** (debe ser invisible si no tiene carnet).
3. **Utilizar elementos avanzados en la vista de formulario:**
    - **`notebook`** para organizar secciones.
    - **`separator`** para separar visualmente los campos.
    - **`attrs`** para hacer condicional la visibilidad del campo "Número de Carnet".

---

## **Vista de Formulario con `notebook`, `separator` y `attrs`**

```xml
<record model="ir.ui.view" id="view_bombero_form">
    <field name="name">Formulario de Bombero</field>
    <field name="model">apellido1.bombero</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="apellido1"/>
                    <field name="apellido2"/>
                    <field name="dni"/>
                    <field name="fecha_nacimiento"/>
                </group>

                <!-- Separador visual -->
                <separator string="Información del Cargo"/>
                
                <group>
                    <field name="puesto"/>
                </group>

                <!-- Uso de Notebook -->
                <notebook>
                    <page string="Historial">
                        <field name="bomberocamion_ids"/>
                    </page>

                    <page string="Carnet de Conducir">
                        <group>
                            <field name="carnet_camion"/>
                            <field name="numero_carnet" attrs="{'invisible': [('carnet_camion', '=', False)]}"/>
                        </group>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
```

---

### **Explicación del Código**

1. **Agrupación de Información en Secciones**

    ```xml
    <group>
        <field name="name"/>
        <field name="apellido1"/>
        <field name="apellido2"/>
        <field name="dni"/>
        <field name="fecha_nacimiento"/>
    </group>
    ```

- Agrupa los datos personales del bombero.

2. **Separador Visual para Organización**

    ```xml
    <separator string="Información del Cargo"/>
    ```

- Muestra una línea separadora con un título.

3. **Uso de `notebook` para Mejor Organización**

    ```xml
    <notebook>
        <page string="Historial">
            <field name="bomberocamion_ids"/>
        </page>
    ```

- **Página "Historial"**: Muestra los camiones en los que ha estado asignado el bombero.

4. **Página de `Carnet de Conducir` con Visibilidad Condicional**

    ```xml
    <page string="Carnet de Conducir">
        <group>
            <field name="carnet_camion"/>
            <field name="numero_carnet" attrs="{'invisible': [('carnet_camion', '=', False)]}"/>
        </group>
    </page>
    ```

- **`attrs="{'invisible': [('carnet_camion', '=', False)]}"`** → Hace que el campo **"Número de Carnet"** solo aparezca si `carnet_camion` está marcado como `True`.

---

### **Resultado Final**

✅ Si el bombero tiene carnet, el campo "Número de Carnet" será visible automáticamente.  
✅ El formulario es más ordenado y amigable gracias al uso de `notebook` y `separator`.  
✅ El historial de asignaciones se encuentra en una pestaña separada.


# 6) Método en la clase bombero. Tenemos la fecha de nacimiento del bombero. Deseamos tener un campo calculado que nos muestre la edad del bombero.


📌 **Requisitos del ejercicio:**
1. **Calcular automáticamente la edad del bombero** a partir de su fecha de nacimiento (`fecha_nacimiento`).
2. **Actualizar la edad en tiempo real** cuando se cambie la fecha de nacimiento en el formulario.
3. **Utilizar `@api.depends`** para recalcular la edad cada vez que `fecha_nacimiento` cambie.
4. **Hacer el código más simple y eficiente** usando `relativedelta` en lugar de cálculos manuales.

---

## **Código Optimizado en el Modelo `Bombero`**

```python
from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta

class Bombero(models.Model):
    _name = 'apellido1.bombero'
    _description = 'Bombero'

    name = fields.Char('Nombre')
    apellido1 = fields.Char('Primer Apellido')
    apellido2 = fields.Char('Segundo Apellido')
    dni = fields.Char('DNI')
    fecha_nacimiento = fields.Date('Fecha de Nacimiento')

    edad = fields.Integer('Edad', compute="_compute_edad")

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        today = date.today()
        for record in self:
            record.edad = relativedelta(today, record.fecha_nacimiento).years 
```

---

### **Explicación del Código**

1. **Campo `edad` con `compute=True`**

    ```python
    edad = fields.Integer('Edad', compute="_compute_edad")
    ```

- **Es un campo calculado** (`compute="_compute_edad"`), lo que significa que no se almacena directamente, sino que se **recalcula automáticamente**.

2. **Decorador `@api.depends('fecha_nacimiento')`**

    ```python
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
    ```

- **Hace que la función `_compute_edad` se ejecute automáticamente** cuando `fecha_nacimiento` cambia.
- **Evita cálculos innecesarios**, ya que solo se ejecuta cuando realmente se necesita.

3. **Cálculo Simplificado de la Edad con `relativedelta`**

    ```python
    today = date.today()
    for record in self:
        record.edad = relativedelta(today, record.fecha_nacimiento).years 
    ```

- Se obtiene la **fecha actual (`date.today()`)**.
- Se usa `relativedelta` para calcular directamente los **años de diferencia** sin hacer comparaciones manuales de mes y día.

---

## **Modificar la Vista de Formulario para Mostrar la Edad**

En el XML de la vista de `Bombero`, agregamos la edad como un campo

```xml
<field name="fecha_nacimiento"/>
<field name="edad"/>
```

- `readonly="1"` NO hace falta poner readonly, puesto que la función viene predefinido
---
### **Resultado Final**

✅ La edad se calcula automáticamente según la fecha de nacimiento.  
✅ Si se cambia la fecha, la edad se actualiza instantáneamente en el formulario.  


# 7) Mediante herencia de clase, crear la siguiente estructura. 

📌 **Requisitos del ejercicio:**
1. **Crear una nueva estructura mediante herencia de clases en Odoo.**
2. **El módulo que hereda se llamará `apellido1_2`.**
3. **Se debe definir la clase `parque` en el módulo heredado.**
4. **Implementar la vista `form` con su `action` y `menuitem`.**
5. **Explicar los conceptos de herencia en Odoo.**

---

## **1. Vista `Form` para la Clase `Parque`**

```xml
<record model="ir.ui.view" id="view_parque_form">
    <field name="name">Formulario de Parque</field>
    <field name="model">apellido1_2.parque</field>
    <field name="arch" type="xml">
        <form>
            <sheet>
                <group>
                    <field name="name"/>
                    <field name="ubicacion"/>
                    <field name="capacidad"/>
                    <field name="jefe_id"/>
                </group>
                <notebook>
                    <page string="Bomberos">
                        <field name="bomberos_ids"/>
                    </page>
                    <page string="Camiones">
                        <field name="camiones_ids"/>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>
```

### **2. Explicación de la Vista `Form`**

- Se agrupan los campos básicos del parque (`name`, `ubicacion`, `capacidad`, `jefe_id`).
- **Se usa un `notebook`** para organizar los bomberos y camiones en pestañas separadas.
- `bomberos_ids` y `camiones_ids` se muestran en sus respectivas pestañas.

---

## **3. `Action` para la Clase `Parque`**

```xml
<record model="ir.actions.act_window" id="action_parque">
    <field name="name">Parques</field>
    <field name="res_model">apellido1_2.parque</field>
    <field name="view_mode">tree,form</field>
</record>
```

📌 **Explicación:**
- Define una acción para abrir la vista del parque.
- Se permite ver la lista (`tree`) y el formulario (`form`).

---

## **4. `Menuitem` para Acceder a `Parque`**

```xml
<menuitem name="Gestión de Parques" id="menu_parques_root" parent="modulo1.modulo1_menu_root"/>
<menuitem name="Parques de Bomberos" id="menu_parques" parent="menu_parques_root" action="action_parque"/>
```

📌 **Explicación:**
- Se crea un **menú raíz** `"Gestión de Parques"`.
- Dentro, un **menú `"Parques de Bomberos"`** que ejecuta la acción para abrir la vista.

---

### **7. Explicación de la Herencia en Odoo**

En este ejercicio, hemos aplicado **herencia en Odoo** al crear un nuevo módulo (`apellido1_2`) que amplía la funcionalidad del sistema existente.

**Tipos de Herencia Usados:**
1. **Herencia de Nuevo Modelo (`_name`)**
    - Se crea un modelo `parque` en `apellido1_2`, sin modificar los modelos originales.
2. **Relaciones con Modelos Existentes**
    - `bomberos_ids` y `camiones_ids` referencian modelos del módulo `apellido1`, extendiendo su funcionalidad sin modificar su estructura original.

---
### **Resultado Final**

✅ Nueva entidad `Parque` creada en `apellido1_2`.  
✅ Formulario con `notebook` para organizar datos.  
✅ Menús y acciones para acceder al módulo desde la interfaz.  
✅ Uso de herencia sin modificar los modelos base (`Bombero`, `Camión`).


# Corrección Chen

[17/2/25, 20:41:43] (ᗜ ˰ ᗜ) XinXing Chen: Vale... Vamos a ir por pasos👀. Para empezar te recomiendo no añadir required o store cuando no te lo piden asi ahorras tiempo. 

- [x] Ejercicio1: La clase bomberocamion tiene 6 campos y se necesita 7, los fechas son Date no datetime( eso es para fecha y hora), el campo puesto esta en la clase de bomberos y lo tienes repetido, yo lo que hice fue poner un campo `fields.Char(related = bombero_id.puesto)`
- [x] Ejercicio 2: En el DNI no pongas unique = True si tienes el constraint puesto
- [x] Ejercicio 4: Esta mal, no te pide eso y no es necesario modificar la vista calendar. Te pide que hagas la función name_get

```python
def name_get(self):
    result = []
    for record in self:
        name = f" {record.bombero_id.name} - {record.camión_id.name}"
		result.append((record.id, name))
    return result
```

- [ ] Ejercicio 5: Si solo te pide hacer el formulario, haz solo eso y no toques nada, no era necesario modificar el model bombero, luego un separator no tiene sentido tener un título puesto que es una línea invisible y creo que en su lugar debiste poner colspan o rowspan
- [x] Ejercicio 6: No pongas readonly en el campo edad porque el compute viene con eso por defecto
- [ ] Ejercicio 7: Sólo te pide que hagas la vista formulario, osea que no tenias que hacerle la clase Parque, y como es una herencia no tiene ni accion ni menuitem porque eso esta en la vista padre
[17/2/25, 20:54:26] (ᗜ ˰ ᗜ) XinXing Chen: te pongo un ejemplo del ejercicio 7
```xml
<record model="ir.ui.view" id="view_parque_form">
    <field name="name">Formulario de Parque</field>
    <field name="model">apellido1.parque</field>
    <field name="inherit_id" ref="apellido1.view_parque_form">
    <field name="arch" type="xml">
            <field name="nombre" position="after">
               <field name="otraClase_id">
            </field>
    </field>
</record>
```

esto es todo lo que tienes que hacer y explicarlo
Total, en general lo tienes bastante bien y apruebas sin problemas asi que enhorabuena👀
