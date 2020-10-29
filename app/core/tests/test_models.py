from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_user_user_with_email_successfull(self):
        #Creating a new user with an email 
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        #Test if the user email is normalized
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email, email.lower())

    def new_user_invalid_email(self):
        #Test creating user with invalid email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_new_superuser(self):
        #Test creating a superuser
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)