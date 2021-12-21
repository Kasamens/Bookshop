from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):

    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(
            username='kojo',
            email='kojo@gmail.com',
            password='kojo'
        )

        self.assertEqual(user.username, 'kojo')
        self.assertEqual(user.email, 'kojo@gmail.com')
        self.assertEqual(user.is_active, True)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@example.com',
            password='superadmin'
        )

        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)