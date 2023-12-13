from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from receipts.models import Receipt

class ReceiptViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_new_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the new view
        response = self.client.get(reverse('receipts:new'))
        self.assertEqual(response.status_code, 200)

    def test_edit_view(self):
        # Create a test receipt
        receipt = Receipt.objects.create(
            store_name='Test Store',
            created_by=self.user,
            date_of_purchase='2023-01-01',
            total_amount=100.00 
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the edit view
        response = self.client.get(reverse('receipts:edit', args=[receipt.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_view(self):
        # Create a test receipt 
        receipt = Receipt.objects.create(
            store_name='Test Store',
            created_by=self.user,
            date_of_purchase='2023-01-01',
            total_amount=100.00  
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the delete view
        response = self.client.post(reverse('receipts:delete', args=[receipt.id]))
        self.assertEqual(response.status_code, 302) 

    def test_list_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the list view
        response = self.client.get(reverse('receipts:list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        # Create a test receipt 
        receipt = Receipt.objects.create(
            store_name='Test Store',
            created_by=self.user,
            date_of_purchase='2023-01-01',
            total_amount=100.00  
        )

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Test the detail view
        response = self.client.get(reverse('receipts:detail', args=[receipt.id]))
        self.assertEqual(response.status_code, 200)
