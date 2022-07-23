from django.test import TestCase 

from conficon_app.models import Profile, Icon, Result

class TestModels(TestCase):
    
    def setUp(self):
        self.Profile = Profile.objects.create(
            email='accounts@gmail.com',
            username='accountowner'
        )

    def test_profile_model_create(self):
        self.assertEquals(self.Profile.username, 'accountowner')
        