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
        fields = '__all__'        
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 5}),
        }