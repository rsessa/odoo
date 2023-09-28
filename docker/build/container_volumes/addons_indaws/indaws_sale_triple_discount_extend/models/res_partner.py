# -*- coding: utf-8 -*-
# Part of Odoo, inDAWS.
# See LICENSE file for full copyright & licensing details.
from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    product_pricelist_customer_ids = fields.One2many(
        comodel_name="product.pricelist.customer",
        inverse_name="partner_id",
        track_visibility="onchange",
        string="Descuentos Familias",
    )
