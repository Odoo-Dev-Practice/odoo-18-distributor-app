from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError
from odoo import Command

class TestPurchaseSecurity(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.PurchaseOrder = cls.env['purchase.order']
        cls.Partner = cls.env['res.partner']

        # Get existing groups
        cls.group_sales = cls.env.ref('asian_distributor.group_asian_distributor_local_sales')
        cls.group_manager = cls.env.ref('asian_distributor.group_asian_distributor_manager')

        # Create Seller User
        cls.seller_user = cls.env['res.users'].create({
            'name': 'Test Seller (Purchase Locked)',
            'login': 'seller_purchase_test_user',
            'groups_id': [Command.set([cls.group_sales.id, cls.env.ref('base.group_user').id])]
        })

        # Create Manager User
        cls.manager_user = cls.env['res.users'].create({
            'name': 'Test Manager (Purchase Allowed)',
            'login': 'manager_purchase_test_user',
            'groups_id': [Command.set([cls.group_manager.id, cls.env.ref('base.group_user').id])]
        })

        # Create Test Vendor
        cls.vendor = cls.Partner.create({'name': 'Test Vendor'})

    def test_01_seller_cannot_create_purchase_order(self):
        """A seller should raise an AccessError when attempting to create a purchase order."""
        with self.assertRaises(AccessError, msg="Sales personnel should not be able to create a purchase order!"):
            self.PurchaseOrder.with_user(self.seller_user).create({
                'partner_id': self.vendor.id,
            })

    def test_02_manager_can_create_purchase_order(self):
        """A manager should be successfully able to create a purchase order."""
        po = self.PurchaseOrder.with_user(self.manager_user).create({
            'partner_id': self.vendor.id,
        })
        self.assertTrue(po.id, "Manager could not create the purchase order.")
