```xml
<odoo>
  <data>
    <!-- Vista -->
    <record model="ir.ui.view" id="minproyect.libro_list">
      <field name="name">Lista de libros</field>
      <field name="model">minproyect.libro</field>
      <field name="arch" type="xml">
       <tree>
          <field name="titulo"/>
        </tree>
      </field>
    </record>


    <!-- Acción para abrir la vista de lista de libros    -->
    <record id="action_libro_list" model="ir.actions.act_window">
      <field name="name">Libros</field>
      <field name="res_model">minproyect.libro</field>
      <field name="view_mode">tree</field>
    </record>


    <!-- Menú raíz   -->
    <!-- Menu de apps instaladas   -->
    <record id="menu_minproyect_root" model="ir.ui.menu">
      <field name="name">Biblioteca de libros</field>
      <field name="sequence">10</field>
    </record>


    <!-- Submenú para libros-->
    <record id="menu_minproyect_libros" model="ir.ui.menu">
      <field name="name">Libros submenu</field>
      <field name="parent_id" ref="menu_minproyect_root"/>
      <field name="action" ref="action_libro_list"/>
    </record>


  </data>
</odoo>
```