from urllib import response
from django.test import TestCase, Client
from ..models import *
from django.urls import reverse

class TestViews(TestCase):
    def setup(self):
        self.client = Client()

   
