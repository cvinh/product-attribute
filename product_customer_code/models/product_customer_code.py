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

from odoo import models, fields


class ProductCustomerCode(models.Model):
    _name = "product.customer.code"
    _description = "Add multiple product customer codes"

    _rec_name = 'product_code'

    product_code = fields.Char(
        string='Customer Product Code',
        required=True,
        help="""This customer's product code will be used when searching into
                a request for quotation.""",
    )

    product_name = fields.Char(
        string='Customer Product Name',
        help="""This customer's product name will be used when searching into
                a request for quotation.""",
    )

    product = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        required=True,
    )

    partner = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True
    )

    company = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=False,
        default=lambda self: self.env['res.company']._company_default_get(),
    )

    _sql_constraints = [
        ('unique_code', 'unique(product_code,company,partner)',
         'Product customer code must be unique'),
    ]

    # TODO: Add index to product_code, partner
