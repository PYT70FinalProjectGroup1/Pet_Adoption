from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model
from .forms import (
    CustomUserCreationForm,
    ServiceForm,
    TreatmentForm,
    AnimalFilterForm,
    AdoptionForm,
    UserProfileUpdateForm,
    AdoptionStoryForm
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animal, Service, Treatment, Adoption, CustomUser, UserProfile, AdoptionStory
from django.views import View   
from django.views.generic import ListView


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        animals = Animal.objects.filter(is_available_for_adoption=True)
        adoption_stories = AdoptionStory.objects.all()
        available_animals = animals.count()

        context["animals"] = animals
        context["adoption_stories"] = adoption_stories
        context["available_animals"] = available_animals

        if self.request.user.is_authenticated:
            try:
                user_location = self.request.user.userprofile.location
                animals_near_user = animals.filter(location=user_location)
                context["animals_near_user"] = animals_near_user
                context["user_location"] = user_location
            except AttributeError:
                context["user_location"] = ""

        return context


class FindAllView(TemplateView):
    template_name = "find_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_pets = Animal.objects.filter(is_available_for_adoption=True)

        filter_form = AnimalFilterForm(self.request.GET)
        if filter_form.is_valid():
            species = filter_form.cleaned_data.get("species")
            breed = filter_form.cleaned_data.get("breed")
            gender = filter_form.cleaned_data.get("gender")
            size = filter_form.cleaned_data.get("size")
            color = filter_form.cleaned_data.get("color")
            min_age = filter_form.cleaned_data.get("min_age")
            max_age = filter_form.cleaned_data.get("max_age")
            location = filter_form.cleaned_data.get("location")

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
    template_name = "find_cats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cats = Animal.objects.filter(
            species__iexact="cat", is_available_for_adoption=True
        )

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            breed = filter_form.cleaned_data.get("breed")
            gender = filter_form.cleaned_data.get("gender")
            size = filter_form.cleaned_data.get("size")
            color = filter_form.cleaned_data.get("color")
            min_age = filter_form.cleaned_data.get("min_age")
            max_age = filter_form.cleaned_data.get("max_age")
            location = filter_form.cleaned_data.get("location")

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
    template_name = "find_dogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dogs = Animal.objects.filter(
            species__iexact="dog", is_available_for_adoption=True
        )

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            breed = filter_form.cleaned_data.get("breed")
            gender = filter_form.cleaned_data.get("gender")
            size = filter_form.cleaned_data.get("size")
            color = filter_form.cleaned_data.get("color")
            min_age = filter_form.cleaned_data.get("min_age")
            max_age = filter_form.cleaned_data.get("max_age")
            location = filter_form.cleaned_data.get("location")

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
    template_name = "find_other_pets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        other_pets = (
            Animal.objects.filter(is_available_for_adoption=True)
            .exclude(species__iexact="cat")
            .exclude(species__iexact="dog")
        )

        show_species = False
        filter_form = AnimalFilterForm(self.request.GET, show_species=show_species)
        if filter_form.is_valid():
            color = filter_form.cleaned_data.get("color")
            breed = filter_form.cleaned_data.get("breed")
            gender = filter_form.cleaned_data.get("gender")
            size = filter_form.cleaned_data.get("size")
            min_age = filter_form.cleaned_data.get("min_age")
            max_age = filter_form.cleaned_data.get("max_age")
            location = filter_form.cleaned_data.get("location")

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
    template_name = "about.html"
    context_object_name = "about"


class DonateView(TemplateView):
    template_name = "donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            logged_user = "Anonymous"
        else:
            logged_user = f"{self.request.user.first_name} {self.request.user.last_name}"

        context["logged_user"] = logged_user
        return context


class MyPetsView(LoginRequiredMixin, ListView):
    model = Adoption
    template_name = "my_pets.html"
    context_object_name = "adoptions"

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
    template_name = "available_services.html"

    def get(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        services = Service.objects.filter(animal=animal)
        context = {"animal": animal, "services": services}
        return render(request, self.template_name, context)


class AvailableTreatmentsView(LoginRequiredMixin, View):
    template_name = "available_treatments.html"

    def get(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        treatments = Treatment.objects.filter(animal=animal)
        context = {"animal": animal, "treatments": treatments}
        return render(request, self.template_name, context)


class AnimalDetailView(DetailView):
    model = Animal
    template_name = "animal_detail.html"
    pk_url_kwarg = "animal_id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_available_adoption = Animal.objects.filter(is_available_for_adoption=True)
        context["other_available_adoption"] = other_available_adoption
        return context


class CreateAdoptionView(LoginRequiredMixin, CreateView):
    model = Adoption
    form_class = AdoptionForm
    template_name = "create_adoption.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.application_status = "Pending"

        animal_id = self.request.GET.get("animal_id")
        if animal_id:
            animal = Animal.objects.get(pk=animal_id)
            form.instance.animal = animal

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home")
    

class AdoptionPendingListView(LoginRequiredMixin, ListView):
    template_name = "adoption_pending_view.html"
    model = Adoption
    context_object_name = "adoption_pending"

    def get_queryset(self):
        return Adoption.objects.filter(application_status="Pending")
    

class ApproveAdoptionView(LoginRequiredMixin, View):
    template_name = "adoption_approval.html"

    def get(self, request, pk):
        adoption = get_object_or_404(Adoption, pk=pk)
        context = {"adoption": adoption}
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        adoption = get_object_or_404(Adoption, pk=pk)
        application_status = request.POST.get("application_status")
        is_approved = request.POST.get("is_approved")
        
        if application_status in ["Accepted"]:
            adoption.application_status = application_status            
            adoption.is_approved = True

            animal = adoption.animal
            animal.is_available_for_adoption = False
            animal.save()            

        elif application_status in ["Denied"]:
            adoption.application_status = application_status            
            adoption.is_approved = False
        
        adoption.save()
            
        return redirect("adoption_pending_list")

class AddAdoptionStoryView(LoginRequiredMixin, View):
    template_name = "add_adoption_story.html"
    form_class = AdoptionStoryForm

    def get(self, request, adoption_pk):
        adoption = get_object_or_404(Adoption, pk=adoption_pk)
        form = self.form_class()
        context = {"adoption": adoption, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, adoption_pk):
        adoption = get_object_or_404(Adoption, pk=adoption_pk)
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(adoption=adoption, user=request.user)
            return redirect('home')

        context = {"adoption": adoption, "form": form}
        return render(request, self.template_name, context)
    
class AdoptionStoriesView(ListView):
    template_name = "adoption_stories.html"
    context_object_name = "adoption_stories"

    def get_queryset(self):
        return AdoptionStory.objects.all()

class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'userprofile_detail.html'
    context_object_name = 'user_profile'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = 'userprofile_update.html'
    context_object_name = 'user_profile'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('userprofile_detail', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        user = get_user_model()
        user_instance = user.objects.get(pk=self.request.user.pk)
        
        form.fields['email'].initial = user_instance.email
        form.fields['first_name'].initial = user_instance.first_name
        form.fields['last_name'].initial = user_instance.last_name
        
        return form

    def form_valid(self, form):
        user = get_user_model()
        user_instance = user.objects.get(pk=self.request.user.pk)
        
        user_instance.first_name = form.cleaned_data['first_name']
        user_instance.last_name = form.cleaned_data['last_name']
        user_instance.save()

        if 'profile_picture' in self.request.FILES:
            user_profile = user_instance.userprofile
            user_profile.profile_picture = self.request.FILES['profile_picture']
            user_profile.save()
        
        return super().form_valid(form)