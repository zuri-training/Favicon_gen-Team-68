from django.test import TestCase, SimpleTestCase
from django.urls import reverse_lazy, reverse, resolve
from ..views import *


class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view, index)