from odoo import models

class Property(models.Model):
  _inherit = 'real.estate.property'

  def action_set_property_as_sold(self):
    print('teste123')

    return super().action_set_property_as_sold()