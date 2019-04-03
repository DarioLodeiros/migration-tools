# Copyright 2019  Pablo Q. Barriuso
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):

    _inherit = 'product.template'

    remote_id = fields.Integer(require=True, copy=False, readonly=True,
            help="ID of the target record in the previous version")
