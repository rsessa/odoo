# -*- coding: utf-8 -*-
# Part of Odoo, inDAWS.
# See LICENSE file for full copyright & licensing details.
from odoo import models, fields


class ProductPricelistCustomer(models.Model):
    _name = "product.pricelist.customer"
    _description = "Product Price-List Customer"
    _sql_constraints = [
        (
            "product_pricelist_customer",
            "unique (category_id,partner_id)",
            "Category must be uniq with customer in Descuentos Familias !!!",
        )
    ]

    category_id = fields.Many2one(
        comodel_name="product.category", string="Categoria de Producto", tracking=True
    )
    discount = fields.Float(string="Descuento %", tracking=True)
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Cliente", tracking=True
    )
