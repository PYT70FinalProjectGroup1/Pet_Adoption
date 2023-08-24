from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DetailView
from .forms import CustomUserCreationForm, ServiceForm, TreatmentForm, AnimalFilterForm, AdoptionForm
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

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        animals = Animal.objects.filter(is_available_for_adoption=True)
        adoptions = Adoption.objects.all()
        available_animals = animals.count()

        context["animals"] = animals
        context["adoptions"] = adoptions
        context["available_animals"] = available_animals

        if self.request.user.is_authenticated:
            try:
                user_location = self.request.user.userprofile.location
                animals_near_user = animals.filter(location=user_location)
                context["animals_near_user"] = animals_near_user
                context["user_location"] = user_location
            except AttributeError:
                default_location = ""
                context["user_location"] = default_location

        return context


class FindAllView(TemplateView):
    template_name = 'find_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_pets = Animal.objects.filter(is_available_for_adoption=True)

        # Process the filter form
        filter_form = AnimalFilterForm(self.request.GET)
        if filter_form.is_valid():
            species = filter_form.cleaned_data.get('species')
            breed = filter_form.cleaned_data.get('breed')
            gender = filter_form.cleaned_data.get('gender')
            size = filter_form.cleaned_data.get('size')
            color = filter_form.cleaned_data.get('color')
            min_age = filter_form.cleaned_data.get('min_age')
            max_age = filter_form.cleaned_data.get('max_age')
            location = filter_form.cleaned_data.get('location')

            if species:
                all_pets = all_pets.filter(species__icontains=species)
            if breed:
                all_pets = all_pets.filter(breed__icontains=breed)
            if gender:
                all_pets = all_pets.filter(gender=gender)
            if size:
                all_pets = all_pets.filter(size=size)
            if color:
                all_pets = all_pets.filter(color__icontains=color)
            if min_age:
                all_pets = all_pets.filter(age__gte=min_age)
            if max_age:
                all_pets = all_pets.filter(age__lte=max_age)
            if location:
                all_pets = all_pets.filter(location=location)

        context["all_pets"] = all_pets
        context["filter_form"] = filter_form
        return context


class FindCatsView(TemplateView):
    template_name = 'find_cats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cats = Animal.objects.filter(species__iexact="cat", is_available_for_adoption=True)

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            breed = filter_form.cleaned_data.get('breed')
            gender = filter_form.cleaned_data.get('gender')
            size = filter_form.cleaned_data.get('size')
            color = filter_form.cleaned_data.get('color')
            min_age = filter_form.cleaned_data.get('min_age')
            max_age = filter_form.cleaned_data.get('max_age')
            location = filter_form.cleaned_data.get('location')

            if breed:
                cats = cats.filter(breed__icontains=breed)
            if gender:
                cats = cats.filter(gender=gender)
            if size:
                cats = cats.filter(size=size)
            if color:
                cats = cats.filter(color__icontains=color)
            if min_age:
                cats = cats.filter(age__gte=min_age)
            if max_age:
                cats = cats.filter(age__lte=max_age)
            if location:
                cats = cats.filter(location=location)

        context["cats"] = cats
        context["filter_form"] = filter_form
        return context


class FindDogsView(TemplateView):
    template_name = 'find_dogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Animal.objects.filter(species__iexact="dog", is_available_for_adoption=True)

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            breed = filter_form.cleaned_data.get('breed')
            gender = filter_form.cleaned_data.get('gender')
            size = filter_form.cleaned_data.get('size')
            color = filter_form.cleaned_data.get('color')
            min_age = filter_form.cleaned_data.get('min_age')
            max_age = filter_form.cleaned_data.get('max_age')
            location = filter_form.cleaned_data.get('location')

            if breed:
                dogs = dogs.filter(breed__icontains=breed)
            if gender:
                dogs = dogs.filter(gender=gender)
            if size:
                dogs = dogs.filter(size=size)
            if color:
                dogs = dogs.filter(color__icontains=color)
            if min_age:
                dogs = dogs.filter(age__gte=min_age)
            if max_age:
                dogs = dogs.filter(age__lte=max_age)
            if location:
                dogs = dogs.filter(location=location)

        context["dogs"] = dogs
        context["filter_form"] = filter_form
        return context


class FindOtherPetsView(TemplateView):
    template_name = 'find_other_pets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        other_pets = Animal.objects.filter(is_available_for_adoption=True) \
            .exclude(species__iexact="cat") \
            .exclude(species__iexact="dog")

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            color = filter_form.cleaned_data.get('color')
            breed = filter_form.cleaned_data.get('breed')
            gender = filter_form.cleaned_data.get('gender')
            size = filter_form.cleaned_data.get('size')
            min_age = filter_form.cleaned_data.get('min_age')
            max_age = filter_form.cleaned_data.get('max_age')
            location = filter_form.cleaned_data.get('location')

            if color:
                other_pets = other_pets.filter(color__icontains=color)
            if breed:
                other_pets = other_pets.filter(breed__icontains=breed)
            if gender:
                other_pets = other_pets.filter(gender=gender)
            if size:
                other_pets = other_pets.filter(size=size)
            if min_age:
                other_pets = other_pets.filter(age__gte=min_age)
            if max_age:
                other_pets = other_pets.filter(age__lte=max_age)
            if location:
                other_pets = other_pets.filter(location=location)

        context["other_pets"] = other_pets
        context["filter_form"] = filter_form
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'


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


class MyPetsView(LoginRequiredMixin, ListView):
    model = Adoption
    template_name = 'my_pets.html'
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


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal_detail.html'
    pk_url_kwarg = 'animal_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_available_adoption = Animal.objects.filter(is_available_for_adoption=True)
        context['other_available_adoption'] = other_available_adoption
        return context


class CreateAdoptionView(LoginRequiredMixin, CreateView):
    model = Adoption
    form_class = AdoptionForm
    template_name = 'create_adoption.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AdoptionStoriesView(LoginRequiredMixin, ListView):    
    template_name = 'adoption_stories.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adoption_stories'] = Adoption.objects.filter(application_status='Accepted')
        return context

    def get_queryset(self):
        return Adoption.objects.filter(application_status='Accepted')