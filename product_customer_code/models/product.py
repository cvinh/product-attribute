# -*- coding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2012 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info@vauxoo.com
############################################################################
#    Coded by: Rodo (rodo@vauxoo.com),Moy (moylop260@vauxoo.com)
############################################################################

from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_customer_codes = fields.One2many(
        comodel_name='product.customer.code',
        inverse_name='product',
        string='Customer Codes',
        copy=False
    )

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        res = super(ProductProduct, self).name_search(
            name=name, args=args, operator=operator, limit=limit)
        if not res:
            partner_id = self._context.get('partner_id')
            if partner_id:
                product_customer_code_obj = self.env['product.customer.code']
                product_codes = product_customer_code_obj.search([
                    ('product_code', '=', name),
                    ('partner', '=', partner_id)
                ], limit=limit)
                return product_codes.product.name_get()
        return res

    @api.multi
    def name_get(self):
        res = super(ProductProduct, self).name_get()
        partner_id = self._context.get('partner_id')
        if partner_id:
            product_customer_code_obj = self.env['product.customer.code']
            for product in self:
                product_code = product_customer_code_obj.search([
                    ('product', '=', product.id),
                    ('partner', '=', partner_id)
                ], limit=1)
                if product_code:
                    # convert tuple to list
                    lst = list(res[0])
                    # change value in the list
                    lst[1] = res[0][1].__add__(' (').__add__(
                        product_code.product_code).__add__(')')
                    # convert list to tuple
                    res[0] = tuple(lst)
        return res
