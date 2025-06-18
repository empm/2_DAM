```python
# -*- coding: utf-8 -*-
from odoo import models, fields


class Libro(models.Model):
     _name = 'minproyect.libro'
     _description = 'Listado de libros'

     titulo = fields.Char(string="Libro")
```