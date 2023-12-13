from django.test import TestCase
from receipts.models import Receipt, User

class ReceiptModelTest(TestCase):
    def test_receipt_creation(self):
        # Create a test user
        user = User.objects.create_user(username='testuser', password='testpassword')
        receipt = Receipt.objects.create(
            store_name='Test Store',
            date_of_purchase='2023-12-15',
            item_list='Item 1, Item 2',
            total_amount=100.0,
            created_by=user
        )


        self.assertEqual(receipt.store_name, 'Test Store')
        self.assertEqual(receipt.date_of_purchase, '2023-12-15')
        self.assertEqual(receipt.item_list, 'Item 1, Item 2')
        self.assertEqual(receipt.total_amount, 100.0)