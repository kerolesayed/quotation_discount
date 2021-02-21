# -*- coding: utf-8 -*-
from odoo import models, fields, api


class quotations_discount(models.Model):
    _inherit = 'sale.order.line'


    disc_value = fields.Monetary("Discount Value", readonly=True, compute='get_disc')

    @api.depends('price_unit', 'discount','product_uom_qty')
    def get_disc(self):
        for r in self:
           r.disc_value = (r.discount/100) * r.price_unit * r.product_uom_qty

class discount(models.Model):
    _inherit = 'sale.order'
    before_disc = fields.Monetary('Before Discount', compute='get_total_disc')
    total_disc = fields.Monetary('Total Discount', compute='get_total_disc')

    @api.depends('order_line.price_unit', 'order_line.disc_value', 'order_line.product_uom_qty')
    def get_total_disc(self):
        for order in self:
           before_disc = total_disc = 0.0
           for line in order.order_line:
                 before_disc += (line.price_unit*line.product_uom_qty)
                 total_disc += line.disc_value
           order.update({
               'before_disc': before_disc,
               'total_disc': total_disc,
           })









