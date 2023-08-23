from datetime import date
from django.test import TestCase
from .models import Animal
# Create your tests here.

class AnimalQueryTest(TestCase):
    def setUp(self):
        Animal.objects.create(name='Kojak', color='Red', species='Fish', breed='Cynix', gender='Male', size='Small', age='2', chip='456789', location='Lodz', about_pet='I like this fish', is_available_for_adoption=True)
        Animal.objects.create(name='Jimmy', color='Black', species='Dog', breed='Neo', gender='Female', size='Medium', age='1', chip='4567891', location='Warsaw', about_pet='I like this dog', is_available_for_adoption=True)
        
    def test_queryset_count(self):
        queryset = Animal.objects.filter(is_available_for_adoption=True, species='Dog')
        self.assertEqual(queryset.count(), 1)
        
    def test_name_in_queryset(self):
        queryset = Animal.objects.filter(is_available_for_adoption=True, species='Dog')
        self.assertTrue(queryset.filter(name="Jimmy").exists())
        
    def test_creation_date_in_queryset(self):
        queryset = Animal.objects.all()
        specific_date = date(2023, 8, 23)
        self.assertTrue(queryset.filter(registration=specific_date).exists())