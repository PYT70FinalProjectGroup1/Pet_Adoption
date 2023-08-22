from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Service, Treatment


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