# -*- coding: utf-8 -*-
# Part of Odoo, inDAWS.
# See LICENSE file for full copyright & licensing details.
from odoo import models, api, fields


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange(
        "product_id", "price_unit", "product_uom", "product_uom_qty", "tax_id"
    )
    def _onchange_first_discount(self):
        if (
            self.product_id
            and self.order_id.partner_id.product_pricelist_customer_ids
            and self.env.user.has_group("product.group_discount_per_so_line")
            and self.order_id.pricelist_id
            and self.order_id.pricelist_id.discount_policy == "without_discount"
        ):
            product_pricelist_customer_id = (
                self.order_id.partner_id.product_pricelist_customer_ids.filtered(
                    lambda l: l.category_id == self.product_id.categ_id
                )
            )
            if product_pricelist_customer_id:
                self.discount = product_pricelist_customer_id.discount

    @api.onchange(
        "product_id", "price_unit", "product_uom", "product_uom_qty", "tax_id"
    )
    def _onchange_second_discount(self):
        if not (
            self.product_id
            and self.product_uom
            and self.order_id.partner_id
            and self.order_id.pricelist_id
            and self.order_id.pricelist_id.discount_policy == "without_discount"
            and self.env.user.has_group("product.group_discount_per_so_line")
        ):
            return

        self.discount2 = 0.0
        product = self.product_id.with_context(
            lang=self.order_id.partner_id.lang,
            partner=self.order_id.partner_id,
            quantity=self.product_uom_qty,
            date=self.order_id.date_order,
            pricelist=self.order_id.pricelist_id.id,
            uom=self.product_uom.id,
            fiscal_position=self.env.context.get("fiscal_position"),
        )

        product_context = dict(
            self.env.context,
            partner_id=self.order_id.partner_id.id,
            date=self.order_id.date_order,
            uom=self.product_uom.id,
        )

        price, rule_id = self.order_id.pricelist_id.with_context(
            product_context
        ).get_product_price_rule(
            self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id
        )
        new_list_price, currency = self.with_context(
            product_context
        )._get_real_price_currency(
            product,
            rule_id,
            self.product_uom_qty,
            self.product_uom,
            self.order_id.pricelist_id.id,
        )

        if new_list_price != 0:
            if self.order_id.pricelist_id.currency_id != currency:
                # we need new_list_price in the same currency as price, which is in the SO's pricelist's currency
                new_list_price = currency._convert(
                    new_list_price,
                    self.order_id.pricelist_id.currency_id,
                    self.order_id.company_id or self.env.company,
                    self.order_id.date_order or fields.Date.today(),
                )
            discount = (new_list_price - price) / new_list_price * 100
            if (discount > 0 and new_list_price > 0) or (
                discount < 0 and new_list_price < 0
            ):
                self.discount2 = discount
