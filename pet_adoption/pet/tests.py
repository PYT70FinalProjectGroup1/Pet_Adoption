from django.test import TestCase
from .models import Animal
# Create your tests here.

class AnimalQuerryTest(TestCase):
    def test_model_queries(self):
        Animal.objects.create(name='Kojak', color='Red', species='Fish',breed='Cynix', gender='Male',size='Small',age='2',chip='456789',location='Lodz',about_pet='I like this fish',is_available_for_adoption=True )
        Animal.objects.create(name='Jimmy', color='Black', species='Dog',breed='Neo', gender='Female',size='Medium',age='1',chip='4567891',location='Warsaw',about_pet='I like this dog',is_available_for_adoption=True )
        
        queryset = Animal.objects.filter(is_available_for_adoption = True, species='Dog')
        self.assertEqual(queryset.count(), 1)
        