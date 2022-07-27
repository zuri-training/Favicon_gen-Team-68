from django.test import SimpleTestCase
from django.urls import reverse, resolve
from conficon_app.views import index


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)
        
