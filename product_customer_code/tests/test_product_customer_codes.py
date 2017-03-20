# -*- coding: utf-8 -*-

from odoo.tests.common import TransactionCase


class TestCustomerCodes(TransactionCase):

    def setUp(self):
        super(TestCustomerCodes, self).setUp()
        self.product_ipad_mini = self.env.ref('product.product_product_6')
        self.partner_agrolait = self.env.ref('base.res_partner_2')

    def test_name_search(self):
        # Add customer code to iPad product
        self.product_ipad_mini.write({
            'product_customer_codes': [(0, 0, {
                'product_code': 'N9TT-9G0A-B7FQ-RANC',
                'partner': self.partner_agrolait.id,
            })],
        })

        # Search product by customer code
        product_obj = self.env['product.product'].with_context({
            'partner_id': self.partner_agrolait.id
        })
        products = product_obj.name_search('N9TT-9G0A-B7FQ-RANC')
        self.assertTrue(len(products) == 1,
                        'Searching by customer code should return one product')
