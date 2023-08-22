from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """Base Model"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta class"""
        abstract = True


class UserProfile(BaseModel):
    """ Class People """

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
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=64, null=False)    
    email = models.EmailField(max_length=64, null=True)
    phone = models.CharField(max_length=32, null=False, unique=True)
    street = models.CharField(max_length=64, null=False)
    location = models.CharField(max_length=32, choices=LOCATION_CHOICE, default="")
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        default="profile_pics/default.jpg",
    )

    class Meta:
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Animal(BaseModel):
    """ Pet Model """
    
    SIZE_CHOICE = [
        ("", "Select Size"),
        ("Small", "Small (0-10kg)"),
        ("Medium", "Medium (11-30kg)"),
        ("Large", "Large (31-50kg)"),
        ("Exter Large", "Extra Large (51kg or more)"),
    ]

    GENDER_CHOICE = [
        ("", "Select Size"),
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
    species = models.CharField(max_length=9, null=False)
    breed = models.CharField(max_length=32, null=False)
    gender = models.CharField(max_length=9, null=False, choices=GENDER_CHOICE, default="")
    size = models.CharField(max_length=32, choices=SIZE_CHOICE, default="")
    age = models.IntegerField()
    chip = models.CharField(max_length=64, unique=True, null=False)
    location = models.CharField(max_length=32, choices=LOCATION_CHOICE, default="")
    registration = models.DateField(default=timezone.now)
    about_pet = models.CharField(max_length=500, null=False)
    image = models.ImageField(upload_to='animal_pics/')
    available_to_adoption = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name


class Adoption(BaseModel):
    """ Adoption model """

    STATUS_CHOICE = [
        ("", "Select Status"),
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Denied", "Denied"),        
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    application_text = models.CharField(max_length=500, null=False)
    application_date = models.DateTimeField(default=timezone.now)
    application_status = models.CharField(max_length=32, choices=STATUS_CHOICE, default="")
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Adoptions"

    def __str__(self):
        return f' {self.application_text} {self.is_approved}'


class Treatment(BaseModel):
    """ Treatments models """

    TREATMENTS_CHOICE = [
        ("", "Select Treatment"),
        ("Vaccination", "Vaccination"),
        ("Deworming", "Deworming"),
        ("Flea and Tick Prevention", "Flea and Tick Prevention"),
        ("Dental Care", "Dental Care"),
        ("Annual Wellness Check-up","Annual Wellness Check-up"),
    ]
    
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_name = models.CharField(choices=TREATMENTS_CHOICE, max_length=64, null=False, default="")
    date = models.DateField(default=timezone.now)
    notes = models.CharField(max_length=500)
    class Meta:
        verbose_name_plural = "Treatments"

    def __str__(self):
        return f'{self.animal.name} {self.treatment_name}'


class Service(BaseModel):
    """ Service models """

    SERVICES_CHOICE = [
        ("", "Select Service"),
        ("Luxury Spa Day", "Luxury Spa Day"),
        ("Canine Massage Therapy", "Canine Massage Therapy"),
        ("Personalized Training Packages", "Personalized Training Packages"),
        ("Pet Photography and Portraits", "Pet Photography and Portraits"),
        ("Pet Parties and Events","Pet Parties and Events"),
        ("VIP Boarding Suites","VIP Boarding Suites"),
        ("Pet Concierge Services","Pet Concierge Services"),
    ]

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    service_name = models.CharField(choices=SERVICES_CHOICE, max_length=64, null=False, default="")
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.animal.name} {self.service_name}'
