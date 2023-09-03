from django.test import TestCase, Client
from django.http import HttpRequest
from django.urls import reverse
from pet.forms import CustomUserCreationForm, ServiceForm, TreatmentForm
from pet.models import Animal, Location
from django.contrib.auth import get_user_model

User = get_user_model()


class TestCustomUserCreationForm(TestCase):
    def setUp(self):
        self.client = Client()

        self.location = Location.objects.create(
            city_key="WAW", city_name="Warsaw")


    def test_get_form(self):
        response = self.client.get(reverse("accounts:register"))
        self.assertEqual(response.status_code, 200)
    

    def test_post_valid_form(self):
        
        form_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "12qwerty12!",
            "password2": "12qwerty12!",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "+48654321890",
            'location':self.location.id,
        }
        response = self.client.post(reverse("accounts:register"), form_data)
        user = User.objects.filter(username='testuser', email='test@example.com').exists()
        self.assertTrue(user)
        self.assertEqual(response.status_code, 302) 

    def test_post_invalid_form(self):
        form_data = {
            "username": "testuser",
            "email": "invalid_email",
            "password1": "password123!",
            "password2": "password456",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "123456789",
            "location": self.location.id,
        }
        response = self.client.post(reverse("accounts:register"), form_data)
        user = User.objects.filter(username='testuser', email='invalid_email').exists()
        self.assertFalse(user)
        self.assertNotEqual(response.status_code, 302)
        self.assertTrue(response.context['form'].errors)
        self.assertIn(b"Enter the same password as before, for verification.", response.content)
        self.assertIn(b"Enter a valid email address", response.content)

    

    def test_post_invalid_the_same_username_form(self):
        from_data1 = User.objects.create_user(
            username="marco",
            email="marco@blue.com",
            password='password123!',
            first_name="John",
            last_name="Doe",
            phone="123456789",
            location=self.location,
        )
        # from_data1.set_password("password123!")
        # from_data1.save()



        form_data = {
            "username": "marco",
            "email": "marco@blue.com",
            "password1": "password123!",
            "password2": "password123!",
            "first_name": "John",
            "last_name": "Doe",
            "phone": "123456789",
            "location": self.location.id,
        }
        response = self.client.post(reverse("accounts:register"), form_data)
        user = User.objects.filter(username='testuser', email='invalid_email').exists()
        self.assertIn(b'A user with that username already exists.', response.content)





