from django.test import TestCase
from .models import Note

class SearchTest(TestCase):
    def setUp(self):
        self.note1 = Note.objects.create(description="this is a note", author = "Note Author")
        self.note2 = Note.objects.create(description="this is another note", author = "Another Note Author")

    def search_notes_on_notes(self):
        response = self.client.get('/notes/', {'search_query':'test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test note.')
        self.assertContains(response, 'Another test note.')

