from django.db import models


class BaseModel(models.Model):
    """Base Model"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta class"""

        abstract = True


class Pet(BaseModel):
    """ Pet Model """

    name = models.CharField(max_length=32, null=False)
    colour = models.CharField(max_length=64, null=False)
    species = models.CharField(max_length=9, null=False)
    chip = models.CharField(max_length=64, unique=True, null=False)
    registration = models.DateField()
    about_pet = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name


class People(BaseModel):
    """ Class Peaple """

    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=64, null=False)
    id_client = models.CharField(max_length=64, unique=True, null=False)
    mail = models.EmailField(max_length=64, null=True)
    phone = models.CharField(max_length=32, null=False, unique=True)
    street = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name + " " + self.surname
