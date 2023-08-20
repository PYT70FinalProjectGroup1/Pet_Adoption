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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=64, null=False)    
    email = models.EmailField(max_length=64, null=True)
    phone = models.CharField(max_length=32, null=False, unique=True)
    street = models.CharField(max_length=64, null=False)
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

    name = models.CharField(max_length=32, null=False)
    colour = models.CharField(max_length=64, null=False)
    species = models.CharField(max_length=9, null=False)
    breed = models.CharField(max_length=32, null=False)
    sex = models.CharField(max_length=9, null=False)
    chip = models.CharField(max_length=64, unique=True, null=False)
    registration = models.DateField(default=timezone.now)
    about_pet = models.TextField()
    image = models.ImageField(upload_to='animal_pics/')
    available_to_adoption = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Animals"

    def __str__(self):
        return self.name


class Adoption(BaseModel):
    """ Adoption model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    application_text = models.TextField()
    application_date = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Adoptions"

    def __str__(self):
        return f' {self.application_text} {self.is_approved}'


class Treatment(BaseModel):
    """ Treatments models """
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_name = models.CharField(max_length=64, null=False)
    date = models.DateField(default=timezone.now)
    notes = models.TextField()
    class Meta:
        verbose_name_plural = "Treatments"

    def __str__(self):
        return f'{self.animal.name} {self.treatment_name}'


class Service(BaseModel):
    """ Services models """

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=32, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return f'{self.animal.name} {self.service_name}'
