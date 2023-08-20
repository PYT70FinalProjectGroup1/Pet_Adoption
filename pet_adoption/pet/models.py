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
    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=64, null=False)
    id_client = models.CharField(max_length=64, unique=True, null=False)
    mail = models.EmailField(max_length=64, null=True)
    phone = models.CharField(max_length=32, null=False, unique=True)
    street = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name + " " + self.surname


class Animal(BaseModel):
    """ Pet Model """

    name = models.CharField(max_length=32, null=False)
    colour = models.CharField(max_length=64, null=False)
    species = models.CharField(max_length=9, null=False)
    breed = models.CharField(max_length=32, null=False)
    sex = models.CharField(max_length=9, null=False)
    chip = models.CharField(max_length=64, unique=True, null=False)
    registration = models.DateField()
    about_pet = models.TextField()
    image = models.ImageField(upload_to='image/')
    available_to_adoption = models.BooleanField()

    def __str__(self):
        return self.name


class Adoption(BaseModel):
    """ Adoption model """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    application_text = models.TextField()
    application_date = models.DateTimeField()
    is_approved = models.BooleanField()

    def __str__(self):
        return self.application_text + ' ' + self.is_approved


class Treatments(BaseModel):
    """ Treatments models """

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_name = models.CharField(max_length=64, null=False)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return self.animal.name + ' ' + self.treatment_name


class Services(BaseModel):
    """ Services models """

    animal = models.ManyToManyField(Animal)
    services = models.CharField(max_length=32, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return self.animal.name + ' ' + self.services
