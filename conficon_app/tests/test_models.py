from django.test import TestCase, SimpleTestCase
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model

#Test forCustom User Model
class NewUserAccountManagerTests(TestCase):
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
             username = 'superadmin', email = 'superadmin@email.com', password = 'testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin ')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

       
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username = 'Tony', email = 'Tony@email.com', password = 'testpass123'
        )
        self.assertEqual(user.username, 'Tony')
        self.assertEqual(user.email, 'Tony@email.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email = '')
        with self.assertRaises(ValueError):
            User.objects.create_user(email = '', password = '')

    
        
