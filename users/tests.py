from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create(
            username = 'Naa',
            email = 'naa@gmail.com',
            password = 'testpass123'
        )
        self.assertEqual(user.username, 'Naa')
        self.assertEqual(user.email, 'naa@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_user_not_created(self):
        User = get_user_model()
        user = User.objects.create(
            username = 'Dede',
            email = 'dede@gmail.com',
            password = 'testpass321',
        )
        self.assertFalse(user.username, 'Dede')
        self.assertFalse(user.email, 'dede@gmail.com')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superadmin',
            email = 'superadmin@gmail.com',
            password = 'testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)