# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import timedelta
import logging


class Trading_shipment(models.Model):
    _name = 'trading.shipment'
    """docstring for shipment_trade"""
    partner_id = fields.Many2one('res.partner', string='Customer', required=False)
    scaduled_date = fields.date(string='scaduled date', default=datetime.now())
    source_document = fields.char(string='source document', required=True)
    state = fields.Selection([
        ('draft', 'draft'),
        ('closed', 'Done'),
    ], default='pr', string='Status')

    raw_material = fields.One2many(comodel_name='trading.product', inverse_name='product_id', string='Raw Materials',
                                   readonly=False)


@api.multi
def do_draft_shipment(self):
    for order in self:
        order.state = 'draft'
    return True


@api.multi
def do_done_shipment(self):
    for order in self:
        order.state = 'closed'
    return True
