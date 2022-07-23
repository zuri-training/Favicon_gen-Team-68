from django.test import SimpleTestCase
from conficon_app.forms import ProfileForm, IconForm

class TestForms(SimpleTestCase):

    def test_form_profile_valid_data(self):
        form = ProfileForm(
            data={
                'email': 'accounts@gmail.com',
                'username': 'accountowner'
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_no_valid(self):
        form = ProfileForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_form_Icon_field_valid_data(self):
        form = IconForm(
            data={
                'image':'file.png'
            }
        )
        self.assertTrue(form.is_valid())

    def test_form_icon_field_no_valid_data(self):
        form = IconForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)