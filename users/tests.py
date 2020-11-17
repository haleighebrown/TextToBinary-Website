from users.models import CustomUser
from django.urls import reverse
from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

# models test
class test_CustomUser(TestCase):

    def test_Create_User(self):
        user = User.objects.create_user(username="Tester", password="12345", email='testing@123.com', age=19, name='user')
        self.assertEqual(user.pk, user.id)
        
    
# Sign up template testing
class test_Sign_Up_View(TestCase):

    def test_SingUp_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
