from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import (
    CustomUserCreationForm,
    UserProfileUpdateForm,
)

from accounts.models import (
    CustomUser,
)


# Create your views here.
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
    success_url = reverse_lazy("accounts:login")

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

    model = CustomUser
    template_name = "userprofile_detail.html"
    context_object_name = "user_profile"
    pk_url_kwarg = "pk"

    def get_queryset(self):
        """
        Retrieve the queryset for the user's profile.

        Returns:
            QuerySet: The queryset containing the user's profile.
        """

        return CustomUser.objects.filter(id=self.request.user.id)


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

    model = CustomUser
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
        return CustomUser.objects.filter(id=self.request.user.id)

    def get_success_url(self):
        """
        Get the URL to redirect to upon successful form submission.

        Returns:
            str: The success URL.
        """
        return reverse_lazy(
            "accounts:userprofile_detail", kwargs={"pk": self.object.pk}
        )

    def get_form(self, form_class=None):
        """
        Customize the form by populating initial values.

        Args:
            form_class: The form class to use.

        Returns:
            Form: The customized form.
        """
        form = super().get_form(form_class)

        user_instance = CustomUser.objects.get(pk=self.request.user.pk)

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

        user_instance = CustomUser.objects.get(pk=self.request.user.pk)

        user_instance.first_name = form.cleaned_data["first_name"]
        user_instance.last_name = form.cleaned_data["last_name"]
        user_instance.save()

        if "profile_picture" in self.request.FILES:
            user_instance.profile_picture = self.request.FILES["profile_picture"]
            user_instance.save()

        return super().form_valid(form)
