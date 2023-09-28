# -*- coding: utf-8 -*-
# Part of Odoo, inDAWS.
# See LICENSE file for full copyright & licensing details.
{
    "name": "Indaws Sale Triple Discount",
    "summary": """
        Customization on triple discount
    """,
    "description": """
    """,
    "author": "inDAWS",
    "website": "http://www.indaws.es",
    "category": "Sales",
    "version": "14.0.1.0.1",
    "sequence": 1,
    "depends": [
        "sale_triple_discount",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_view.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
