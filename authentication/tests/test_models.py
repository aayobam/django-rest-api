from rest_framework.test import APITestCase
from authentication.models import User



class TestModel(APITestCase):
    def test_create_userl(self):
        user = User.objects.create_user(username="aayobam", email="aayobam@gmail", password="password1234@01")
        self.assertEqual(user.username, "aayobam")
        self.assertEqual(user.email, "aayobam@gmail.com")
        self.assertEqual(user.password, "password1234@01")
        self.assertIsInstance(user, User)