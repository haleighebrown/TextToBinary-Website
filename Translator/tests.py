from Translator.models import Translation
from django.utils import timezone
from django.urls import reverse
from django.test import SimpleTestCase, TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User = get_user_model()

# models test
class TranslationTest(TestCase):

    def Create_Translation(self, title="test", Input="Testing!", Output="Still Testing!"):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')
        return Translation.objects.create(title=title, Input=Input, Output=Output, choice='----------', date=timezone.now(), author=self.user)

    def test_Translation_creation(self):
        t = self.Create_Translation()
        self.assertTrue(isinstance(t, Translation))
        self.assertEquals(t.title, "test")
        self.assertEquals(t.Input, "Testing!")
        self.assertEquals(t.Output, "Still Testing!")
        self.assertEquals(t.choice, '----------')
        self.assertEquals(t.author, self.user)

#list view test to insure the list appears correctly
    def test_Translation_list_view(self):
        t = self.Create_Translation()
        resp = self.client.get(reverse('translation_list'))
        self.assertEqual(resp.status_code, 200)

#edit view test to make sure all fields are filled
    def test_Translation_edit_view(self):
        t = self.Create_Translation()
        self.assertTrue(isinstance(t, Translation))
        self.assertIsNotNone(t.title)
        self.assertIsNotNone(t.Input)
        self.assertIsNotNone(t.Output)
        self.assertIsNotNone(t.choice)
        self.assertIsNotNone(t.author)
        self.assertIsNotNone(t.date)

#create view test to make sure fields ar not left unchanged
    def test_Translation_create_view(self):
        t = self.Create_Translation()
        self.assertTrue(isinstance(t, Translation))
        self.assertNotEquals(t.title, "")
        self.assertNotEquals(t.Input, "")
        self.assertNotEquals(t.Output, "")
        self.assertNotEquals(t.author, "")
        self.assertNotEquals(t.date, "")
        self.assertNotEquals(t.choice, "-------------")

#detail view tests to make sure all details appear 
    def test_Translation_detail_view(self):
        t = self.Create_Translation()
        self.assertTrue(isinstance(t, Translation))
        self.assertIsNotNone(t.title)
        self.assertIsNotNone(t.Input)
        self.assertIsNotNone(t.Output)
        self.assertIsNotNone(t.choice)
        self.assertIsNotNone(t.author)
        self.assertIsNotNone(t.date)

#delete view test to make sure there is a translation to delete
    def test_Translation_delete_view(self):
        t = self.Create_Translation()
        self.assertIsNotNone(t)
        
        

    
        
        
