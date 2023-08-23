from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Service, Treatment, Animal, UserProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]


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
    color = forms.CharField(max_length=64, required=False)
    breed = forms.CharField(max_length=32, required=False)
    gender = forms.ChoiceField(choices=Animal.GENDER_CHOICE, required=False)
    size = forms.ChoiceField(choices=Animal.SIZE_CHOICE, required=False)
    min_age = forms.IntegerField(required=False)
    max_age = forms.IntegerField(required=False)
    location = forms.ChoiceField(choices=Animal.LOCATION_CHOICE, required=False)


class QuestionForm(forms.Form):

    members = forms.ModelMultipleChoiceField(
        queryset=UserProfile.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    adopt = forms.ChoiceField(choices=Animal.SPECIES_CHOICE, required=False)
    why_do_you_want_to_adopt = forms.CharField(max_length=500, required=False)
    how_do_you_like_spend_time = forms.CharField(max_length=500, required=False)
    what_will_happen_to_the_pet = forms.CharField(max_length=500, required=False)
    street = forms.CharField(max_length=64, required=False)
    city = forms.CharField(max_length=64, required=False)
    house_or_apartment = forms.ChoiceField(choices=[
        ('House', 'House'),
        ('Apartment', 'Apartment')
    ],
        widget=forms.RadioSelect)
    m2 = forms.CharField(max_length=9, required=False)
    ever_pet = forms.ChoiceField(choices=[
        ('Yes', 'Yes'),
        ('No', 'No')
    ],
        widget=forms.RadioSelect)
