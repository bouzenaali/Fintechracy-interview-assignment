from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class AuthenticationViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_index_view_authenticated_user(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('authentication:index'))
        self.assertEqual(response.status_code, 302) 

    def test_index_view_unauthenticated_user(self):
        response = self.client.get(reverse('authentication:index'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_get(self):
        response = self.client.get(reverse('authentication:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_post_invalid_form(self):
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'invalid'}
        response = self.client.post(reverse('authentication:signup'), data)
        self.assertEqual(response.status_code, 200)

    def test_signup_view_post_valid_form(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',  
            'password1': 'StrongPassword123',  
            'password2': 'StrongPassword123',  
        }
        response = self.client.post(reverse('authentication:signup'), data)

        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('authentication:logout'))
        self.assertEqual(response.status_code, 302) 
