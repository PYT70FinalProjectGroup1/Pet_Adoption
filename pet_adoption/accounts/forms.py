from django import forms
from django.contrib.auth.forms import UserCreationForm
from pet.models import (
    Location,
)
from accounts.models import (
    CustomUser,
)
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that extends UserCreationForm to include additional fields.

    Attributes:
        email (forms.EmailField): Field for user's email.
        first_name (forms.CharField): Field for user's first name.
        last_name (forms.CharField): Field for user's last name.
        phone (PhoneNumberField): Field for user's phone number.
        location (forms.ModelChoiceField): Field for selecting user's location.
        profile_picture (forms.ImageField): Field for user's profile picture.

    Methods:
        save(commit=True): Create a new user instance along with their associated profile.
    """

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name", max_length=32, required=True)
    last_name = forms.CharField(label="Last Name", max_length=64, required=True)
    phone = PhoneNumberField()
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),
        required=True,
    )
    profile_picture = forms.ImageField(
        label="Profile Picture",
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": False}),
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone",
            "location",
            "profile_picture",
        ]

    def save(self, commit=True):
        """
        Create a new user instance along with their associated profile.

        Args:
            commit (bool): Whether to commit the changes to the database.

        Returns:
            CustomUser: The newly created user instance.
        """
        user = super().save(commit=False)

        profile_picture = self.cleaned_data.get("profile_picture")
        if not profile_picture:
            user.profile_picture = "profile_pics/default.jpg"

        if commit:
            user.save()
        return user


class UserProfileUpdateForm(forms.ModelForm):
    """
    A form for updating user profile information.

    Attributes:
        email: Email field for the user.
        first_name: First name field for the user.
        last_name: Last name field for the user.

        class Meta: Define the model and fields to include.

    """

    email = forms.EmailField(label="Email")
    first_name = forms.CharField(max_length=32, label="First Name")
    last_name = forms.CharField(max_length=32, label="Last Name")

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "first_name",
            "last_name",
            "phone",
            "location",
            "profile_picture",
        ]
