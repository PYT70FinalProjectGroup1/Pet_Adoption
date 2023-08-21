from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal

# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        animals = Animal.objects.all()
        context["animals"] = animals

        return context


class AboutView(LoginRequiredMixin,TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DonateView(LoginRequiredMixin,TemplateView):
    template_name = 'donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logged_user = f'{self.request.user.userprofile.first_name} {self.request.user.userprofile.last_name}'
        context['logged_user'] = logged_user        
        return context