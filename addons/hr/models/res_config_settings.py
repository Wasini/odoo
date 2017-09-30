# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_id = fields.Many2one(
    	'res.company', string='Company',
        default=lambda self: self.env.user.company_id, required=True)
    resource_calendar_id = fields.Many2one(
        'resource.calendar', 'Company Working Hours',
        related='company_id.resource_calendar_id')
    module_hr_org_chart = fields.Boolean(string="Show Organizational Chart")
