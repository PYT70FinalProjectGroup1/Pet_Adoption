from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import get_user_model, get_user
from .forms import (
    CustomUserCreationForm,
    ServiceForm,
    TreatmentForm,
    AnimalFilterForm,
    AdoptionForm,
    UserProfileUpdateForm,
    AdoptionStoryForm,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
    Animal,
    Service,
    Treatment,
    Adoption,
    CustomUser,
    UserProfile,
    AdoptionStory,
)
from django.views import View
from django.views.generic import ListView
from django.db.models import Q


class RegisterView(CreateView):
    """
    A view for user registration.

    Attributes:
        form_class (CustomUserCreationForm): The form class for user registration.
        template_name (str): The template name to render for user registration.
        success_url (str): The URL to redirect to upon successful registration.

    Methods:
        form_valid(form): Overrides the default form_valid method to perform additional actions.
    """

    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        """
        Handle valid form submission.

        Args:
            form (CustomUserCreationForm): The submitted form instance.

        Returns:
            HttpResponse: The response after successful form validation.
        """

        response = super().form_valid(form)
        return response


class HomeView(TemplateView):
    """
    A view for the home page.

    Attributes:
        template_name (str): The template name to render for the home page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

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
    """
    A view for finding and filtering available pets.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "find_all.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

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
    """
    A view for finding and filtering available cats.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "find_cats.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

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
    """
    A view for finding and filtering available dogs.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "find_dogs.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

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
    """
    A view for finding and filtering available pets of species other than cats and dogs.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "find_other_pets.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

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
    """
    A view for displaying information about the website or organization.

    Attributes:
        template_name (str): The template name to render for the page.
        context_object_name (str): The name used to refer to the context data in the template.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "about.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        return context


class DonateView(TemplateView):
    """
    A view for displaying information about donating on the website.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get_context_data(**kwargs): Overrides the default get_context_data method to provide context data to the template.
    """

    template_name = "donate.html"

    def get_context_data(self, **kwargs):
        """
        Provide context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: A dictionary containing context data for rendering the template.
        """

        context = super().get_context_data(**kwargs)
        if not self.request.user.is_authenticated:
            logged_user = "Anonymous"
        else:
            logged_user = (
                f"{self.request.user.first_name} {self.request.user.last_name}"
            )

        context["logged_user"] = logged_user
        return context


class MyPetsView(LoginRequiredMixin, ListView):
    """
    A view for displaying a list of approved adoptions related to the logged-in user.

    Attributes:
        model (Model): The model to use for the queryset.
        template_name (str): The template name to render for the page.
        context_object_name (str): The name used to refer to the context data in the template.

    Methods:
        get_queryset(): Overrides the default get_queryset method to return the filtered queryset.
    """

    model = Adoption
    template_name = "my_pets.html"
    context_object_name = "adoptions"

    def get_queryset(self):
        """
        Get the queryset of approved adoptions related to the logged-in user.

        Returns:
            QuerySet: The filtered queryset of approved adoptions.
        """
        return Adoption.objects.filter(user=self.request.user, is_approved=True)


class CreateServiceView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new service related to a specific animal.

    Attributes:
        model (Model): The model to use for creating the new service.
        form_class (Form): The form class to use for the service creation.
        template_name (str): The template name to render for the page.

    Methods:
        get_success_url(): Returns the URL to redirect to after successful form submission.
        form_valid(form): Overrides the default form_valid method to save additional data.
    """

    model = Service
    form_class = ServiceForm
    template_name = "create_service.html"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: The URL to redirect to.
        """

        animal_id = self.kwargs["animal_id"]
        return reverse("services", args=[animal_id])

    def form_valid(self, form):
        """
        Process the form submission and save additional data.

        Args:
            form (Form): The submitted form instance.

        Returns:
            HttpResponse: The response after form submission.
        """

        animal_pk = self.kwargs["animal_id"]
        animal = Animal.objects.get(pk=animal_pk)

        form.instance.animal = animal
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class CreateTreatmentView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new treatment related to a specific animal.

    Attributes:
        model (Model): The model to use for creating the new treatment.
        form_class (Form): The form class to use for the treatment creation.
        template_name (str): The template name to render for the page.

    Methods:
        get_success_url(): Returns the URL to redirect to after successful form submission.
        form_valid(form): Overrides the default form_valid method to save additional data.
    """

    model = Treatment
    form_class = TreatmentForm
    template_name = "create_treatment.html"

    def get_success_url(self):
        """
        Get the URL to redirect to after successful form submission.

        Returns:
            str: The URL to redirect to.
        """

        animal_id = self.kwargs["animal_id"]
        return reverse("treatments", args=[animal_id])

    def form_valid(self, form):
        """
        Process the form submission and save additional data.

        Args:
            form (Form): The submitted form instance.

        Returns:
            HttpResponse: The response after form submission.
        """

        animal_pk = self.kwargs["animal_id"]
        animal = Animal.objects.get(pk=animal_pk)

        form.instance.animal = animal
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


class AvailableServicesView(LoginRequiredMixin, View):
    """
    A view for displaying available services related to a specific animal.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get(request, pk): Handles the GET request and renders the page with data.
    """

    template_name = "available_services.html"

    def get(self, request, pk):
        """
        Handle the GET request and render the page with data.

        Args:
            request (HttpRequest): The GET request instance.
            pk (int): The primary key of the animal for which services are displayed.

        Returns:
            HttpResponse: The rendered page with context data.
        """

        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        services = Service.objects.filter(animal=animal)
        context = {"animal": animal, "services": services}
        return render(request, self.template_name, context)


class AvailableTreatmentsView(LoginRequiredMixin, View):
    """
    A view for displaying available treatments related to a specific animal.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get(request, pk): Handles the GET request and renders the page with data.
    """

    template_name = "available_treatments.html"

    def get(self, request, pk):
        """
        Handle the GET request and render the page with data.

        Args:
            request (HttpRequest): The GET request instance.
            pk (int): The primary key of the animal for which treatments are displayed.

        Returns:
            HttpResponse: The rendered page with context data.
        """

        animal = get_object_or_404(Animal, pk=pk, adoption__user=request.user)
        treatments = Treatment.objects.filter(animal=animal)
        context = {"animal": animal, "treatments": treatments}
        return render(request, self.template_name, context)


class AnimalDetailView(DetailView):
    """
    A detail view for displaying information about a specific animal.

    Attributes:
        model: The model class for the view to work with.
        template_name (str): The template name to render for the page.
        pk_url_kwarg (str): The keyword argument name for the primary key in the URL.

    Methods:
        get_context_data(**kwargs): Get additional context data to be used in the template.
        post(request, animal_id): Handle the POST request for adding/removing animals from favorites.
    """

    model = Animal
    template_name = "animal_detail.html"
    pk_url_kwarg = "animal_id"

    def get_context_data(self, **kwargs):
        """
        Get additional context data to be used in the template.

        Returns:
            dict: The context data dictionary.
        """

        context = super().get_context_data(**kwargs)
        other_available_adoption = Animal.objects.filter(is_available_for_adoption=True)
        context["other_available_adoption"] = other_available_adoption

        if self.request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user=self.request.user)
            context["user_favourite_animals"] = user_profile.favorites.all()

        return context

    def post(self, request, animal_id):
        """
        Handle the POST request for adding/removing animals from favorites.

        Args:
            request (HttpRequest): The POST request instance.
            animal_id (int): The primary key of the animal being favorited/unfavorited.

        Returns:
            HttpResponseRedirect: Redirects back to the animal detail page.
        """

        animal = get_object_or_404(Animal, id=animal_id)
        user_profile = request.user.userprofile

        if user_profile.favorites.filter(id=animal.id).exists():
            user_profile.favorites.remove(animal)
        else:
            user_profile.favorites.add(animal)

        return redirect("animal_detail", animal_id=animal.id)


class CreateAdoptionView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new adoption application.

    Attributes:
        model: The model class for the view to work with.
        form_class: The form class to use for creating the adoption application.
        template_name (str): The template name to render for the page.

    Methods:
        form_valid(form): Process the valid form data before saving.
        get_success_url(): Get the URL to redirect to after a successful form submission.
    """

    model = Adoption
    form_class = AdoptionForm
    template_name = "create_adoption.html"

    def form_valid(self, form):
        """
        Process the valid form data before saving.

        Args:
            form (AdoptionForm): The valid form instance containing the data.

        Returns:
            HttpResponse: A response after processing the form data.
        """

        form.instance.user = self.request.user
        form.instance.application_status = "Pending"

        animal_id = self.request.GET.get("animal_id")
        if animal_id:
            animal = Animal.objects.get(pk=animal_id)
            form.instance.animal = animal

        return super().form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect to after a successful form submission.

        Returns:
            str: The URL to redirect to.
        """

        return reverse("home")


class AdoptionPendingListView(LoginRequiredMixin, ListView):
    """
    A view to display a list of pending adoption applications.

    Attributes:
        template_name (str): The template name to render for the page.
        model: The model class for the view to work with.
        context_object_name (str): The name to use for the context variable containing the query results.

    Methods:
        get_queryset(): Get the queryset of pending adoption applications to display.
    """

    template_name = "adoption_pending_view.html"
    model = Adoption
    context_object_name = "adoption_pending"

    def get_queryset(self):
        """
        Get the queryset of pending adoption applications to display.

        Returns:
            QuerySet: The queryset of pending adoption applications.
        """

        return Adoption.objects.filter(application_status="Pending")


class ApproveAdoptionView(LoginRequiredMixin, View):
    """
    A view to approve or deny an adoption application.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get(request, pk): Handle the GET request to display the adoption approval form.
        post(request, pk): Handle the POST request to approve or deny the adoption application.
    """

    template_name = "adoption_approval.html"

    def get(self, request, pk):
        """
        Handle the GET request to display the adoption approval form.

        Args:
            request: The HTTP GET request.
            pk (int): The primary key of the Adoption object.

        Returns:
            HttpResponse: The rendered HTML template with the adoption details.
        """

        adoption = get_object_or_404(Adoption, pk=pk)
        context = {"adoption": adoption}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        """
        Handle the POST request to approve or deny the adoption application.

        Args:
            request: The HTTP POST request.
            pk (int): The primary key of the Adoption object.

        Returns:
            HttpResponseRedirect: Redirects to the adoption pending list.
        """

        adoption = get_object_or_404(Adoption, pk=pk)
        application_status = request.POST.get("application_status")
        is_approved = request.POST.get("is_approved")

        if application_status in ["Approved"]:
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
    """
    A view to allow users to add adoption stories.

    Attributes:
        template_name (str): The template name to render for the page.
        form_class (class): The form class for creating adoption stories.

    Methods:
        get(request, adoption_pk): Handle the GET request to display the adoption story form.
        post(request, adoption_pk): Handle the POST request to save the adoption story.
    """

    template_name = "add_adoption_story.html"
    form_class = AdoptionStoryForm

    def get(self, request, adoption_pk):
        """
        Handle the GET request to display the adoption story form.

        Args:
            request: The HTTP GET request.
            adoption_pk (int): The primary key of the Adoption object.

        Returns:
            HttpResponse: The rendered HTML template with the adoption story form.
        """

        adoption = get_object_or_404(Adoption, pk=adoption_pk)
        form = self.form_class()
        context = {"adoption": adoption, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, adoption_pk):
        """
        Handle the POST request to save the adoption story.

        Args:
            request: The HTTP POST request.
            adoption_pk (int): The primary key of the Adoption object.

        Returns:
            HttpResponseRedirect: Redirects to the home page after saving the story.
            HttpResponse: Renders the HTML template with errors if form is invalid.
        """

        adoption = get_object_or_404(Adoption, pk=adoption_pk)
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save(adoption=adoption, user=request.user)
            return redirect("home")

        context = {"adoption": adoption, "form": form}
        return render(request, self.template_name, context)


class AdoptionStoriesView(ListView):
    """
    A view to display a list of adoption stories.

    Attributes:
        template_name (str): The template name to render for the page.
        context_object_name (str): The name of the context variable containing the list of adoption stories.

    Methods:
        get_queryset(): Retrieve the queryset of all adoption stories.
    """

    template_name = "adoption_stories.html"
    context_object_name = "adoption_stories"

    def get_queryset(self):
        """
        Retrieve the queryset of all adoption stories.

        Returns:
            QuerySet: The queryset containing all adoption stories.
        """

        return AdoptionStory.objects.all()


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """
    A view to display the details of a user's profile.

    Attributes:
        model: The model class for the user profile.
        template_name (str): The template name to render for the page.
        context_object_name (str): The name of the context variable containing the user profile.
        pk_url_kwarg (str): The name of the URL keyword argument to capture the user profile's primary key.

    Methods:
        get_queryset(): Retrieve the queryset for the user's profile.
    """

    model = UserProfile
    template_name = "userprofile_detail.html"
    context_object_name = "user_profile"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """
        Retrieve the queryset for the user's profile.

        Returns:
            QuerySet: The queryset containing the user's profile.
        """

        return UserProfile.objects.filter(user=self.request.user)


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    A view to update a user's profile information.

    Attributes:
        model: The model class for the user profile.
        form_class: The form class to use for updating the profile.
        template_name (str): The template name to render for the page.
        context_object_name (str): The name of the context variable containing the user profile.
        pk_url_kwarg (str): The name of the URL keyword argument to capture the user profile's primary key.

    Methods:
        get_queryset(): Retrieve the queryset for the user's profile.
        get_success_url(): Get the URL to redirect to upon successful form submission.
        get_form(form_class=None): Customize the form by populating initial values.
        form_valid(form): Save the user's first name, last name, and profile picture (if provided).
    """

    model = UserProfile
    form_class = UserProfileUpdateForm
    template_name = "userprofile_update.html"
    context_object_name = "user_profile"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """
        Retrieve the queryset for the user's profile.

        Returns:
            QuerySet: The queryset containing the user's profile.
        """
        return UserProfile.objects.filter(user=self.request.user)

    def get_success_url(self):
        """
        Get the URL to redirect to upon successful form submission.

        Returns:
            str: The success URL.
        """
        return reverse_lazy("userprofile_detail", kwargs={"pk": self.object.pk})

    def get_form(self, form_class=None):
        """
        Customize the form by populating initial values.

        Args:
            form_class: The form class to use.

        Returns:
            Form: The customized form.
        """
        form = super().get_form(form_class)

        user = get_user_model()
        user_instance = user.objects.get(pk=self.request.user.pk)

        form.fields["email"].initial = user_instance.email
        form.fields["first_name"].initial = user_instance.first_name
        form.fields["last_name"].initial = user_instance.last_name

        return form

    def form_valid(self, form):
        """
        Save the user's first name, last name, and profile picture (if provided).

        Args:
            form: The form containing the updated data.

        Returns:
            HttpResponse: The response after successful form validation.
        """
        user = get_user_model()
        user_instance = user.objects.get(pk=self.request.user.pk)

        user_instance.first_name = form.cleaned_data["first_name"]
        user_instance.last_name = form.cleaned_data["last_name"]
        user_instance.save()

        if "profile_picture" in self.request.FILES:
            user_profile = user_instance.userprofile
            user_profile.profile_picture = self.request.FILES["profile_picture"]
            user_profile.save()

        return super().form_valid(form)


class AnimalFavouriteListView(LoginRequiredMixin, View):
    """
    A view to display the list of favourite animals for the logged-in user.

    Attributes:
        template_name (str): The template name to render for the page.

    Methods:
        get(request): Get the list of favourite animals for the logged-in user.
    """

    template_name = "animal_favourite_list.html"

    def get(self, request):
        """
        Get the list of favourite animals for the logged-in user.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The rendered template with the list of favourite animals in the context.
        """
        favourite_animals = request.user.userprofile.favorites.all()
        context = {"favourite_animals": favourite_animals}
        return render(request, self.template_name, context)


class MyAdoptionFormsView(LoginRequiredMixin, ListView):
    """
    A view to display the adoption forms submitted by the logged-in user.

    Attributes:
        model (Model): The model to query for adoption forms.
        template_name (str): The template name to render for the page.
        context_object_name (str): The context variable name for the queryset.

    Methods:
        get_queryset(): Get the queryset of adoption forms submitted by the logged-in user.
    """

    model = Adoption
    template_name = "my_adoption_forms.html"
    context_object_name = "adoption_forms"

    def get_queryset(self):
        """
        Get the queryset of adoption forms submitted by the logged-in user.

        Returns:
            QuerySet: The queryset of adoption forms submitted by the user.
        """
        return Adoption.objects.filter(user=self.request.user)


class AnimalSearchView(TemplateView):
    template_name = 'animal_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        searched = self.request.GET.get('searched')
        
        find_pets = Animal.objects.filter(is_available_for_adoption=True)

        if searched is not None and searched.strip() != "":
            find_pets =find_pets.filter(
                Q(species__icontains=searched) | Q(breed__icontains=searched)| Q(name__icontains=searched),is_available_for_adoption=True
            )
        else:
            find_pets = Animal.objects.none()

        context['find_pets'] = find_pets        
        return context


