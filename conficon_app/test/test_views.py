from django.test import TestCase, Client
from django.urls import reverse

from conficon_app.models import Profile, Icon, Result

class Testviews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.register_url = reverse('signup')
        self.login_url = reverse('login')

        self.user={
            'username': 'accountowner',
            'email': 'accounts@gmail.com',
            'password1': 'password',
            'password2': 'password',
        }

        self.user_short_password={
           'username': 'accountowner',
            'email': 'accounts@gmail.com',
            'password1': 'pas',
            'password2': 'pas', 
        }

        self.user_unmatching_password={
            'username': 'accountowner',
            'email': 'accounts@gmail.com',
            'password1': 'password',
            'password2': 'passwordo',
        }

        self.user_Invalid_email={
            'username': 'accountowner',
            'email': 'accounts.com',
            'password1': 'password',
            'password2': 'passwordo',
        }
        return super().setUp()
# test the get request of the views

    def test_project_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_signup_page_correct(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_user_can_signup_correctly(self):
        response = self.client.post(self.register_url, self.user, format='text/html')

        self.assertEquals(response.status_code, 302) 

    def test_user_cant_register_with_short_password(self):
        response = self.client.post(self.register_url, self.user_short_password, format='text/html')

        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.user_short_password['password1'], self.user_short_password['password2'])

    def test_user_password_is_not_the_same(self):
        response = self.client.post(self.register_url, self.user_unmatching_password, format='text/html')

        self.assertEquals(response.status_code, 302)
        self.assertEqual(self.user_short_password['password1'], self.user_short_password['password2'])

    def test_user_cant_register_with_invalid_email(self):
        response = self.client.post(self.register_url, self.user_Invalid_email, format='text/html')
        
        self.assertEquals(response.status_code, 302)

    def test_user_cannot_signup_with_already_taken_email(self):
        self.client.post(self.register_url, self.user, format='text/html')

        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 302)

    # def test_user_with_message_user_already_exists(self):
    #     self.client.post(self.register_url, self.user, format='text/html')
    #     with self.assertRaisesMessage(error, "User exists, please login"):
    #         self.client.post(self.register_url, self.user, format='text/html')

class TestLogin(Testviews):

    def test_login_view_page_correct(self):
        response = self.client.get(self.login_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_authenticate_user(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = Profile.objects.filter(email=self.user['email']).first()
        user.is_active = True
        user.save()
        response = self.client.post(self.login_url, self.user, format='text/html')

        self.assertEquals(response.status_code, 302)

    def test_cant_login_authenticate_user_with_unverified_email(self):
        self.client.post(self.register_url, self.user, format='text/html')
        user = Profile.objects.filter(email=self.user['email']).first()

        response = self.client.post(self.login_url, self.user, format='text/html')

        self.assertEquals(response.status_code, 302)

    # def test_cant_login_authenticate_user_without_username(self):
        
    #     response = self.client.post(self.login_url, {'username':' ', 'password':'password'}, format='text/html')

    #     self.assertEqual(response.status_code, 401)

    # def test_cant_login_authenticate_user_without_password(self):
    #     response = self.client.post(self.login_url, {'username': 'accounts@gmail.com', 'password':' '}, format='text/html')

    #     self.assertEqual(response.status_code, 401)
