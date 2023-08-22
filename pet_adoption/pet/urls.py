from django.urls import path
from .views import HomeView, AboutView, DonateView, AdoptedAnimalsView, AvailableServicesView, CreateServiceView,AvailableTreatmentsView,  CreateTreatmentView, FindCatsView, FindDogsView, FindOtherPetsView, FindAllView,RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("donate", DonateView.as_view(), name="donate"),

    path("adopted_animals/", AdoptedAnimalsView.as_view(), name="adopted_animals"),
    
    path("services/<int:pk>/", AvailableServicesView.as_view(), name="services"),
    path("create_service/<int:animal_id>/",CreateServiceView.as_view(),name="create_service"),

    path("treatments/<int:pk>/", AvailableTreatmentsView.as_view(), name="treatments"),
    path("create_treatment/<int:animal_id>/",CreateTreatmentView.as_view(),name="create_treatment"),

    path("find/cats", FindCatsView.as_view(), name="find_cats"),
    path("find/dogs", FindDogsView.as_view(), name="find_dogs"),
    path("find/other_pets", FindOtherPetsView.as_view(), name="find_other_pets"),
    path("find/all_pets", FindAllView.as_view(), name="find_all_pets"),
    
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]