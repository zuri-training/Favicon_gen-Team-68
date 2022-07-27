from django.test import SimpleTestCase
from conficon_app.forms import UserCreationForm, UserChangeForm

class TestForms(SimpleTestCase):

    def test_form_profile_valid_data(self):
        form = UserCreationForm(
            data={
                'email': 'accounts@gmail.com',
                'username': 'accountowner'
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_form_no_valid(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())
        # self.assertEquals(len(form.errors), 3)

    def test_profile_change_form_valid(self):
        form = UserChangeForm(
            data={
                'username': 'accountowner'
            }
        )
        self.assertTrue(form.is_valid())
    def test_profile_change_form_not_valid(self):
        form = UserChangeForm(data={})