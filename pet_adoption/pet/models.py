from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(BaseModel):

    LOCATION_CHOICE = [
        ("", "Select Location"),
        ("Warsaw", "WAW"),
        ("Krakow", "KRK"),
        ("Wroclaw", "WRO"),
        ("Poznan", "POZ"),
        ("Lodz", "LDZ"),
        ("Gdansk", "GDA"),
        ("Szczecin", "SCZ"),
        ("Bydgoszcz", "BGD"),
        ("Katowice", "KAT"),
        ("Gdynia", "GDY"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=32, null=False)
    location = models.CharField(
        max_length=32, choices=LOCATION_CHOICE, default="", null=False
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=False,
        null=False,
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

    LOCATION_CHOICE = [
        ("", "Select Location"),
        ("Warsaw", "WAW"),
        ("Krakow", "KRK"),
        ("Wroclaw", "WRO"),
        ("Poznan", "POZ"),
        ("Lodz", "LDZ"),
        ("Gdansk", "GDA"),
        ("Szczecin", "SCZ"),
        ("Bydgoszcz", "BGD"),
        ("Katowice", "KAT"),
        ("Gdynia", "GDY"),
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
    location = models.CharField(
        max_length=32, blank=False, choices=LOCATION_CHOICE, default=""
    )
    about_pet = models.TextField(max_length=500, null=False)
    image = models.ImageField(upload_to="animal_pics/")
    is_available_for_adoption = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name


class Adoption(BaseModel):

    RESIDENCE_TYPE_CHOICE = [
        ("", "Select Status"),
        ("House", "House"),
        ("Apartment", "Apartment"),
    ]

    FIRST_PET_CHOICES = [("", "Select Status"), ("Yes", "Yes"), ("No", "No")]

    STATUS_CHOICE = [
        ("", "Select Status"),
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Denied", "Denied"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    city = models.CharField(max_length=64, null=False, default="")
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
