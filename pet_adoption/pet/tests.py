from django.test import TestCase
from .models import Animal, Location
from django.test import TestCase


class AnimalQueryTest(TestCase):
    def setUp(self):
        self.location = Location.objects.create(city_key="WAW", city_name="Warsaw")

        Animal.objects.create(
            name="Kojak",
            color="Red",
            species="Fish",
            breed="Cynix",
            gender="Male",
            size="Small",
            age="2",
            chip="456789",
            location=self.location,
            about_pet="I like this fish",
            is_available_for_adoption=True,
        )

        Animal.objects.create(
            name="Jimmy",
            color="Black",
            species="Dog",
            breed="Neo",
            gender="Female",
            size="Medium",
            age="1",
            chip="4567891",
            location=self.location,
            about_pet="I like this dog",
            is_available_for_adoption=True,
        )

    def test_filter_dogs_available_for_adoption(self):
        queryset = Animal.objects.filter(is_available_for_adoption=True, species="Dog")
        self.assertEqual(queryset.count(), 1)

    def test_jimmy_exists_with_filter(self):
        queryset = Animal.objects.filter(is_available_for_adoption=True, species="Dog")
        self.assertTrue(queryset.filter(name="Jimmy", location=self.location).exists())

    def test_kojak_not_exists_with_filter(self):
        queryset = Animal.objects.filter(is_available_for_adoption=True, species="Dog")
        self.assertFalse(queryset.filter(name="Kojak", location=self.location).exists())