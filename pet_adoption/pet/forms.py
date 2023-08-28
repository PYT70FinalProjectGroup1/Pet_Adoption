from django import forms
from django.contrib.auth.forms import UserCreationForm
from pet.models import (
    Service,
    Treatment,
    Animal,
    Adoption,
    Location,
    AdoptionStory,
)
from accounts.models import CustomUser
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


class ServiceForm(forms.ModelForm):
    """
    A form for creating or updating a Service instance.

    Attributes:
        Meta (class): Nested class defining metadata options for the form.

    Methods:
        save(commit=True, animal=None): Create or update a Service instance.
    """

    class Meta:
        model = Service
        exclude = ("animal",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

    def save(self, commit=True, animal=None):
        """
        Create or update a Service instance.

        Args:
            commit (bool): Whether to commit the changes to the database.
            animal (Animal, optional): The associated Animal instance.

        Returns:
            Service: The created or updated Service instance.
        """
        instance = super().save(commit=False)

        if animal is not None:
            instance.animal = animal

        if commit:
            instance.save()

        return instance


class TreatmentForm(forms.ModelForm):
    """
    A form for creating or updating a Treatment instance.

    Attributes:
        Meta (class): Nested class defining metadata options for the form.

    Methods:
        save(commit=True, animal=None): Create or update a Treatment instance.
    """

    class Meta:
        model = Treatment
        exclude = ("animal",)
        widgets = {
            "next_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 5}),
        }

    def save(self, commit=True, animal=None):
        """
        Create or update a Treatment instance.

        Args:
            commit (bool): Whether to commit the changes to the database.
            animal (Animal, optional): The associated Animal instance.

        Returns:
            Treatment: The created or updated Treatment instance.
        """
        instance = super().save(commit=False)

        if animal is not None:
            instance.animal = animal

        if commit:
            instance.save()

        return instance


class AnimalFilterForm(forms.Form):
    """
    A form for filtering animal search results based on various criteria.

    Attributes:
        species (CharField): Field for specifying the species of animals.
        breed (CharField): Field for specifying the breed of animals.
        gender (ChoiceField): Field for selecting the gender of animals.
        size (ChoiceField): Field for selecting the size of animals.
        color (CharField): Field for specifying the color of animals.
        min_age (IntegerField): Field for specifying the minimum age of animals.
        max_age (IntegerField): Field for specifying the maximum age of animals.
        location (ModelChoiceField): Field for selecting the location of animals.

    Methods:
        __init__(self, *args, show_species=True, **kwargs): Initialize the form.
    """

    species = forms.CharField(max_length=32, required=False)
    breed = forms.CharField(max_length=32, required=False)
    gender = forms.ChoiceField(choices=Animal.GENDER_CHOICE, required=False)
    size = forms.ChoiceField(choices=Animal.SIZE_CHOICE, required=False)
    color = forms.CharField(max_length=64, required=False)
    min_age = forms.IntegerField(required=False)
    max_age = forms.IntegerField(required=False)
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),
        required=False,
    )

    def __init__(self, *args, show_species=True, **kwargs):
        """
        Initialize the form.

        Args:
            show_species (bool): Whether to show the species field (default is True).
        """
        super().__init__(*args, **kwargs)
        if not show_species:
            self.fields["species"].widget = forms.HiddenInput()


class AdoptionForm(forms.ModelForm):
    """
    A form for creating adoption applications.

    Attributes:
        class Meta: Define the model and excluded fields.

    Methods:
        save(self, commit=True, animal=None, user=None): Save the form instance.
    """

    class Meta:
        model = Adoption
        exclude = ("animal", "user", "application_status", "is_approved")

    def save(self, commit=True, animal=None, user=None):
        """
        Save the form instance.

        Args:
            commit (bool): Whether to commit the instance to the database (default is True).
            animal: The animal to which the adoption application is related.
            user: The user submitting the adoption application.

        Returns:
            instance: The saved instance of the adoption application.
        """
        instance = super().save(commit=False)

        if animal and user is not None:
            instance.animal = animal
            instance.user = user

        if commit:
            instance.save()

        return instance


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


class AdoptionStoryForm(forms.ModelForm):
    """
    A form for creating an adoption story associated with an adoption instance.

    Attributes:
        class Meta: Define the model and fields to include.

    """

    class Meta:
        model = AdoptionStory
        exclude = ("adoption",)

    def save(self, commit=True, adoption=None, user=None):
        """
        Save the adoption story instance with the associated adoption and user.

        Args:
            commit (bool): Whether to save the instance immediately.
            adoption: The adoption instance to associate the story with.
            user: The user associated with the adoption.

        Returns:
            AdoptionStory: The saved adoption story instance.

        """
        instance = super().save(commit=False)

        if adoption and user:
            instance.adoption = adoption

        if commit:
            instance.save()

        return instance
