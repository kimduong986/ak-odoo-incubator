# Copyright 2023 Akretion (https://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class ProductSupplierinfoGroup(models.Model):
    _inherit = "product.supplierinfo.group"
    _order = "sequence, product_definition_precision desc, id"
