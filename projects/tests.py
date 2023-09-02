from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Note
import unittest
import sqlite3
from .views import signupView


class SearchTestCase(TestCase):
    def setUp(self):
        self.note1 = Note.objects.create(description="this is a note", author = "Note Author")
        self.note2 = Note.objects.create(description="this is another note", author = "Another Note Author")

    def test_search_notes_on_notes(self):
        response = self.client.get('/notes', {'search_query':'test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this is a note')
        self.assertContains(response, 'this is another note')

class TestSigninPage(TestCase):
    def setUp(self):
        # Create a test user
        self.username = 'testUser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_sign_in_valid_user(self):
        # Test signing in with valid credentials
        response = self.client.post(reverse('signup'), {'username': self.username, 'password': self.password})
        

        # Check if the user is authenticated
        authenticated_user = authenticate(username=self.username, password=self.password)
        self.assertTrue(authenticated_user is not None and authenticated_user.is_authenticated)

        # Check if the response redirects to the home page
        self.assertRedirects(response, reverse('home'))

    """ How to implement a Invalid User Test:
    def test_sign_in_invalid_user(self):
        # Test signing in with invalid credentials
        response = self.client.post(reverse('signup'), {'username': 'invalidUser', 'password': 'invalidPassword'})
        
        # Check if the response does not redirect (sign-in should fail)
        self.assertEqual(response.status_code, 200)

        # Check if the user is not authenticated
        self.assertFalse(self.user.is_authenticated)"""

if __name__ == "__main__":
    unittest.main()

       