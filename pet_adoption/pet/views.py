from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm, ServiceForm, TreatmentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal, Service, Treatment, Adoption
from django.views import View
from django.views.generic import ListView

# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        animals = Animal.objects.filter(available_to_adoption = True)
        available_animals = animals.count()

        context["animals"] = animals
        context["available_animals"] = available_animals

        if self.request.user.is_authenticated:
            user_location = self.request.user.userprofile.location
            animals_near_user = animals.filter(location=user_location)
            context["animals_near_user"] = animals_near_user
            context["user_location"] = user_location
            
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DonateView(TemplateView):
    template_name = 'donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            logged_user = "Anonymous"
        else:
            logged_user = f'{self.request.user.userprofile.first_name} {self.request.user.userprofile.last_name}'
        
        context['logged_user'] = logged_user        
        return context

class AdoptedAnimalsView(LoginRequiredMixin, ListView):
    model = Adoption    
    template_name = 'adopted_animals.html'
    context_object_name = 'adoptions'

    def get_queryset(self):
        return Adoption.objects.filter(user=self.request.user, is_approved=True)

class CreateServiceView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "create_service.html"

    def get_success_url(self):
        animal_id = self.kwargs["animal_id"]
        return reverse("services", args=[animal_id])

    def form_valid(self, form):
        animal_pk = self.kwargs["animal_id"]
        animal = Animal.objects.get(pk=animal_pk)
        
        form.instance.animal = animal
        form.instance.user = self.request.user
        form.save()        
        return super().form_valid(form)

class CreateTreatmentView(LoginRequiredMixin, CreateView):
    model = Treatment
    form_class = TreatmentForm
    template_name = "create_treatment.html"

    def get_success_url(self):
        animal_id = self.kwargs["animal_id"]
        return reverse("treatments", args=[animal_id])

    def form_valid(self, form):
        animal_pk = self.kwargs["animal_id"]
        animal = Animal.objects.get(pk=animal_pk)
        
        form.instance.animal = animal
        form.instance.user = self.request.user
        form.save()        
        return super().form_valid(form)


class AvailableServicesView(LoginRequiredMixin, View):
    template_name = 'available_services.html'

    def get(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        services = Service.objects.filter(animal=animal)        
        context = {'animal': animal, 'services': services}
        return render(request, self.template_name, context)

class AvailableTreatmentsView(LoginRequiredMixin, View):
    template_name = 'available_treatments.html'

    def get(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        treatments = Treatment.objects.filter(animal=animal)        
        context = {'animal': animal, 'treatments': treatments}
        return render(request, self.template_name, context)