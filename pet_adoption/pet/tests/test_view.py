from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from pet.models import Animal, Adoption, AdoptionStory, Location
from pet.forms import CustomUserCreationForm

class PetAppTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.location = Location.objects.create(
            city_key="WAW", city_name="Warsaw")

        self.animal = Animal.objects.create(
            name='Test Animal',
            color='black',
            species='dog',
            breed='Garfild',
            gender='male',
            size='small',
            age=2,
            chip='12321312',
            location=self.location,
            image='animal_pics/Billy.jpg',
            about_pet='bla bla',
            is_available_for_adoption=True
        )

        self.adoption = Adoption.objects.create(
            user=self.user,
            animal=self.animal,
            application_text='blabalbal',
            application_status='Pending',
            reason_for_adoption='dbaslkbndlas',
            time_spending_habbit='dnisaondoias',
            pet_fate='bdsiuabuid',
            street='ba7s89d',
            city=self.location,
            living_space='House',
            square_meters='dbuiasd',
            initial_pet='Yes',
            is_approved=True

        )

        self.adoption_story = AdoptionStory.objects.create(
            adoption=self.adoption,
            story_title='Test adoption story',
            story_description='bnsduibasiud',
            
        )

    def test_register_view(self):
        url = reverse('accounts:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_animal_model(self):
        animal = Animal.objects.get(name='Test Animal')
        self.assertEqual(animal.name, 'Test Animal')