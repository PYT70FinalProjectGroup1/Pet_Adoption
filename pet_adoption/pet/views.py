from django.shortcuts import render
from .models import UserProfile, Animal, Services, Treatments, Adoption
from django.views.generic import ListView, FormView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.

class AnimalListView(ListView):
    template_name = 'animals_list.html'
    model = Animal


class UserProfileListView(ListView):
    template_name = 'users_list.html'
    model = UserProfile


class AdoptionListView(ListView):
    template_name = 'adoptions_list.html'
    model = Adoption
