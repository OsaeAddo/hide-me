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
