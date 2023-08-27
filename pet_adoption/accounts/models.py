from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    A custom user model extending Django's AbstractUser with an additional 'phone' field.

    Fields:
        phone (PhoneNumberField): The user's phone number.

    You can further extend this class by adding any other fields you need in your custom user model.

    Methods:
        __str__(): Returns a string representation of the user by their username.
    """

    phone = PhoneNumberField(null=True, blank=True)
    location = models.ForeignKey(
        "pet.Location", max_length=255, null=True, on_delete=models.CASCADE
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/",
        null=True,
        default="profile_pics/default.jpg",
    )

    def __str__(self):
        return self.username
