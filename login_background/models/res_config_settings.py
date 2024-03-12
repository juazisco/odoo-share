# -*- coding: utf-8 -*-
from odoo import api, fields, models, modules


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    style = fields.Selection([('default', 'Default'), ('left', 'Left'), ('right', 'Right'), ('middle', 'Middle')], help='Select Background Theme')
    background = fields.Selection([('image', 'Image'), ('color', 'Color')], default='color', help='Select Background Theme')
    background_image = fields.Many2one('login.image', string="Background Image", help='Select Background Image For Login Page')
    color = fields.Char(string="Background Color", help="Choose your Background color")
    display_info = fields.Text(string="Información Login", help="Ingrese texto en HTML")
    second_logo_image = fields.Many2one('login.image', string="Second Logo Image", help='Select Second logo Image For Login Page')
    

    @api.onchange('background')
    def onchange_background(self):
        if self.background == 'image':
            self.color = False
        elif self.background == 'color':
            self.background_image = False
        else:
            self.background_image = self.color = False

    @api.onchange('style')
    def onchange_style(self):
        if self.style == 'default' or self.style is False:
            self.background = self.background_image = self.color = False

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        image_id = int(self.env['ir.config_parameter'].sudo().get_param('login_background.background_image'))
        second_logo_image_id = int(self.env['ir.config_parameter'].sudo().get_param('login_background.second_logo_image'))
        res.update(
            background_image=image_id,
            #second_logo_image=second_logo_image_id,
            color=self.env['ir.config_parameter'].sudo().get_param('login_background.color'),
            background=self.env['ir.config_parameter'].sudo().get_param('login_background.background'),
            style=self.env['ir.config_parameter'].sudo().get_param('login_background.style'),
            display_info=self.env['ir.config_parameter'].sudo().get_param('login_background.display_info'),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()

        set_image = self.background_image.id or False
        set_image_logo = self.second_logo_image.id or False
        set_color = self.color or False
        set_background = self.background or False
        set_style = self.style or False
        set_display_info = self.display_info or False
        param.set_param('login_background.background_image', set_image)
        param.set_param('login_background.second_logo_image', set_image_logo)
        param.set_param('login_background.color', set_color)
        param.set_param('login_background.background', set_background)
        param.set_param('login_background.style', set_style)
        param.set_param('login_background.display_info', set_display_info)
