from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Service, Treatment, Animal


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
    location = forms.ChoiceField(choices=Animal.LOCATION_CHOICE, required=False)


    def __init__(self, *args, show_species=True,**kwargs):
        super().__init__(*args, **kwargs)
        if not show_species:
            self.fields['species'].widget = forms.HiddenInput()