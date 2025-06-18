<!-- VISTA FORMULARIO -->
<record id="view_form_estudiante" model="ir.ui.view">
    <field name="name">academia.estudiante.form</field>
    <field name="model">academia.estudiante</field>
    <field name="arch" type="xml">
        <form string="Estudiante" groups="base.group_user"> <!-- Solo para usuarios internos -->
            <sheet>
                <group>
                    <field name="nombre"/>
                    <field name="apellido"/>
                    <field name="dni"/>
                    <field name="estado" readonly="1"/> <!-- Campo solo lectura -->
                    <field name="pais_usuario" groups="base.group_system"/> <!-- Solo para administradores -->
                </group>
                <group>
                    <field name="fecha_nacimiento"/>
                    <field name="edad" readonly="1"/>
                    <field name="nota_examen"/>
                    <field name="aprobado" readonly="1"/>
                </group>
                <notebook>
                    <page string="Cursos">
                        <field name="curso_ids" widget="many2many_tags"/>
                    </page>
                    <page string="Calificaciones">
                        <field name="calificaciones_ids">
                            <tree editable="bottom">
                                <field name="nota"/>
                                <field name="comentario"/>
                            </tree>
                        </field>
                    </page>
                </notebook>
            </sheet>
        </form>
    </field>
</record>

<!-- VISTA DE ARBOL/LISTA --> 
<record id="view_tree_estudiante" model="ir.ui.view">
    <field name="name">academia.estudiante.tree</field>
    <field name="model">academia.estudiante</field>
    <field name="arch" type="xml">
        <tree string="Estudiantes">
            <field name="nombre"/>
            <field name="apellido"/>
            <field name="edad"/>
            <field name="nota_examen"/>
            <field name="aprobado"/>
            <field name="estado"/>
            <field name="pais_usuario"/>
        </tree>
    </field>
</record>

<!-- VISTA DE CALENDARIO -->
<record id="view_calendar_estudiante" model="ir.ui.view">
    <field name="name">academia.estudiante.calendar</field>
    <field name="model">academia.estudiante</field>
    <field name="arch" type="xml">
        <calendar string="Calendario de Estudiantes"
                  date_start="fecha_nacimiento"
                  date_stop="fecha_fin_estimada"
                  color="estado">
            <field name="nombre"/>
            <field name="edad" invisible="1"/>
            <field name="aprobado" readonly="1"/>
        </calendar>
    </field>
</record>

<!-- VISTA DE BÚSQUEDA -->
<record id="view_search_estudiante" model="ir.ui.view">
    <field name="name">academia.estudiante.search</field>
    <field name="model">academia.estudiante</field>
    <field name="arch" type="xml">
        <search string="Buscar Estudiantes">
            <field name="nombre"/>
            <field name="apellido"/>
            <field name="estado"/>
            <field name="pais_usuario"/>
            <filter string="Aprobados" name="filter_aprobados" domain="[('aprobado', '=', True)]"/>
            <filter string="Activos" name="filter_activos" domain="[('estado', '=', 'activo')]" context="{'group_by': 'estado'}"/>
        </search>
    </field>
</record>

<!-- VISTA DE GRÁFICO -->
<record id="view_graph_estudiante" model="ir.ui.view">
    <field name="name">academia.estudiante.graph</field>
    <field name="model">academia.estudiante</field>
    <field name="arch" type="xml">
        <graph string="Gráfico de Estudiantes" type="bar">
            <!-- Agrupar por país de usuario y mostrar nota -->
            <field name="pais_usuario" type="row"/>
            <field name="estado" type="col"/>
            <field name="nota_examen" type="measure"/>
        </graph>
    </field>
</record>

#Descripción rápida:
type="bar": define el tipo de gráfico (puede ser bar, line o pie).

type="row": campo por el que se agruparán las filas (en este caso, el país del usuario).

type="col": agrupa por columnas (estado del estudiante, por ejemplo activo, baja, etc.).

type="measure": campo numérico para calcular y representar gráficamente (nota del examen).