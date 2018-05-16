# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Clear ICT Solutions <info@clearict.com>.
#    All Rights Reserved.
#       @author: Michael Telahun Makonnen <miket@clearict.com>
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    
    partner_contact = fields.Many2one('res.partner', 'Contacto')

    @api.onchange('partner_id')
    def onchange_partner_id(self):

        res = super(SaleOrder, self).onchange_partner_id()
        for so in self:
            if not res:
                res = {}
            #if not res.has_key('value'):
            if not 'value' in res:
                res.update({'value': {}})
            res['value'].update({'partner_contact': False})
            so.partner_contact = False
        return res
