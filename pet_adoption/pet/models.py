from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CustomUser(AbstractUser):
    phone = PhoneNumberField(null=True, blank=True)
    # Add any other fields you need in your custom user model

    def __str__(self):
        return self.username

class Location(BaseModel):
    city_key = models.CharField(max_length=3, null=False)
    city_name = models.CharField(max_length=32, null=False)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.city_name}"


class UserProfile(BaseModel):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone = PhoneNumberField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to="profile_pics/",        
        null=True,
        default="profile_pics/default.jpg",
    )

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"{self.user}"


class Animal(BaseModel):

    SPECIES_CHOICE = [
        ("", "Select Species"),
        ("Dog", "Dog"),
        ("Cat", "Cat"),
        ("Other", "Other"),
    ]

    SIZE_CHOICE = [
        ("", "Select Size"),
        ("Small", "Small (0-10kg)"),
        ("Medium", "Medium (11-30kg)"),
        ("Large", "Large (31-50kg)"),
        ("Exter Large", "Extra Large (51kg or more)"),
    ]

    GENDER_CHOICE = [
        ("", "Select Gender"),
        ("Male", "Male"),
        ("Female", "Female"),
    ]


    name = models.CharField(max_length=32, null=False)
    color = models.CharField(max_length=64, null=False)
    species = models.CharField(
        max_length=9, blank=False, choices=SPECIES_CHOICE, default=""
    )
    breed = models.CharField(max_length=32, null=False)
    gender = models.CharField(
        max_length=9, null=False, blank=False, choices=GENDER_CHOICE, default=""
    )
    size = models.CharField(max_length=32, blank=False, choices=SIZE_CHOICE, default="")
    age = models.IntegerField(null=False)
    chip = models.CharField(max_length=64, unique=True, null=False)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    about_pet = models.TextField(max_length=500, null=False)
    image = models.ImageField(upload_to="animal_pics/")
    is_available_for_adoption = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name


class Adoption(BaseModel):

    RESIDENCE_TYPE_CHOICE = [
        ("", "Select Type"),
        ("House", "House"),
        ("Apartment", "Apartment"),
    ]

    FIRST_PET_CHOICES = [("", "Select Choice"), ("Yes", "Yes"), ("No", "No")]

    STATUS_CHOICE = [
        ("", "Select Status"),
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Denied", "Denied"),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    application_text = models.TextField(max_length=500, null=False)
    application_date = models.DateTimeField(auto_now_add=True)
    application_status = models.CharField(
        max_length=32, choices=STATUS_CHOICE, blank=False, null=False, default=""
    )
    reason_for_adoption = models.TextField(null=False, default="")
    time_spending_habbit = models.TextField(null=False, default="")
    pet_fate = models.TextField(null=False, default="")
    street = models.CharField(max_length=64, null=False, default="")
    city = models.ForeignKey(Location,on_delete=models.CASCADE)
    living_space = models.CharField(
        max_length=32, choices=RESIDENCE_TYPE_CHOICE, null=False, blank=False, default=""
    )
    square_meters = models.CharField(max_length=9, null=False, default="")
    initial_pet = models.CharField(
        max_length=32, choices=FIRST_PET_CHOICES, null=False, blank=False, default=""
    )
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Adoptions"

    def __str__(self):
        return f" {self.id} - {self.is_approved}"


class Treatment(BaseModel):

    TREATMENTS_CHOICE = [
        ("", "Select Treatment"),
        ("Vaccination", "Vaccination"),
        ("Deworming", "Deworming"),
        ("Flea and Tick Prevention", "Flea and Tick Prevention"),
        ("Dental Care", "Dental Care"),
        ("Annual Wellness Check-up", "Annual Wellness Check-up"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_name = models.CharField(
        choices=TREATMENTS_CHOICE, max_length=64, null=False, blank=False, default=""
    )
    next_date = models.DateField(null=False)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Treatments"

    def __str__(self):
        return f"{self.animal.name}_{self.treatment_name}"


class Service(BaseModel):

    SERVICES_CHOICE = [
        ("", "Select Service"),
        ("Luxury Spa Day", "Luxury Spa Day"),
        ("Canine Massage Therapy", "Canine Massage Therapy"),
        ("Personalized Training Packages", "Personalized Training Packages"),
        ("Pet Photography and Portraits", "Pet Photography and Portraits"),
        ("Pet Parties and Events", "Pet Parties and Events"),
        ("VIP Boarding Suites", "VIP Boarding Suites"),
        ("Pet Concierge Services", "Pet Concierge Services"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    service_name = models.CharField(
        choices=SERVICES_CHOICE, max_length=64, null=False, blank=False, default=""
    )
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.animal.name}_{self.service_name}"

class AdoptionStory(BaseModel):
    adoption = models.OneToOneField(Adoption, on_delete=models.CASCADE)
    story_title = models.CharField(max_length=128, null=False)
    story_description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Adoption Stories"

        def __str__(self):
            return f"{self.story_title}"