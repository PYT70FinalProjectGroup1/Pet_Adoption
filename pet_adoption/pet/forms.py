from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Service, Treatment, Animal, UserProfile, Adoption, Location, CustomUser
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name", max_length=32, required=True)
    last_name = forms.CharField(label="Last Name", max_length=64, required=True)
    phone = PhoneNumberField()
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),  # Provide the queryset for available locations
        required=True,
    )
    profile_picture = forms.ImageField(
        label="Profile Picture",
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
        user = super().save(commit=False)

        user_profile = UserProfile(
            user=user,
            phone=self.cleaned_data["phone"],
            location=self.cleaned_data["location"],
            profile_picture=self.cleaned_data["profile_picture"],
        )

        if commit:
            user.save()
            user_profile.save()
        return user


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ("animal",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

    def save(self, commit=True, animal=None):
        instance = super().save(commit=False)

        if animal is not None:
            instance.animal = animal

        if commit:
            instance.save()

        return instance


class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        exclude = ("animal",)
        widgets = {
            "next_date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 5}),
        }

    def save(self, commit=True, animal=None):
        instance = super().save(commit=False)

        if animal is not None:
            instance.animal = animal

        if commit:
            instance.save()

        return instance


class AnimalFilterForm(forms.Form):
    species = forms.CharField(max_length=32, required=False)
    breed = forms.CharField(max_length=32, required=False)
    gender = forms.ChoiceField(choices=Animal.GENDER_CHOICE, required=False)
    size = forms.ChoiceField(choices=Animal.SIZE_CHOICE, required=False)
    color = forms.CharField(max_length=64, required=False)
    min_age = forms.IntegerField(required=False)
    max_age = forms.IntegerField(required=False)
    location = forms.ModelChoiceField(
        label="Location",
        queryset=Location.objects.all(),  # Provide the queryset for available locations
        required=True,
    )

    def __init__(self, *args, show_species=True, **kwargs):
        super().__init__(*args, **kwargs)
        if not show_species:
            self.fields["species"].widget = forms.HiddenInput()


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        exclude = ("animal", "user" ,"application_status","is_approved")

    def save(self, commit=True, animal=None, user=None):
        instance = super().save(commit=False)

        if animal and user is not None:
            instance.animal = animal
            instance.user = user

        if commit:
            instance.save()

        return instance
