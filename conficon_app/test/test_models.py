from django.test import TestCase 

from conficon_app.models import Profile, Icon, Result

class TestModels(TestCase):

    def test_profile_model_create_user(self):
        user = Profile.objects.create_user('accountowner', 'accounts@gmail.com', 'password1234')

        self.assertIsInstance(user, Profile)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'accounts@gmail.com')
    
    def test_profile_model_create_super_user(self):
        user = Profile.objects.create_superuser('accountowner', 'accounts@gmail.com', 'password1234')
        
        self.assertIsInstance(user, Profile)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'accounts@gmail.com')

    def test_raises_error_when_no_username(self):
        self.assertRaises(ValueError, Profile.objects.create_user, username='', email='accounts@gmail.com', password='password1234')


    def test_raises_error_with_message_when_no_username(self):
        with self.assertRaisesMessage(ValueError, "Username is required!"):
            Profile.objects.create_user(username='', email='accounts@gmail.com', password='password1234')

    def test_raises_error_when_no_email(self):
        self.assertRaises(ValueError, Profile.objects.create_user, username='accountowner', email='', password='password1234' )

    def test_raises_error_with_message_when_no_email(self):
        with self.assertRaisesMessage(ValueError, "Email address is required!"):
            Profile.objects.create_user(username='accountowner', email='', password='password1234')

    def test_create_superuser_with_superuser_status_is_staff(self):
        with self.assertRaisesMessage(ValueError, "Superuser must be assigned to is_staff=True"):
            Profile.objects.create_superuser(username='accountowner', email='accounts@gmail.com', password='password1234', is_staff=False)

    def test_create_superuser_with_superuser_status_is_superuser(self):
        with self.assertRaisesMessage(ValueError, "Superuser must be assigned to is_superuser=True"):
            Profile.objects.create_superuser(username='accountowner', email='accounts@gmail.com', password='password1234', is_superuser=False)