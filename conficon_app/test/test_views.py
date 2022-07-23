from django.test import TestCase, Client
from django.urls import reverse

from conficon_app.models import Profile, Icon, Result
import json

class Testviews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')

# test the get request of the views

    def test_project_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    