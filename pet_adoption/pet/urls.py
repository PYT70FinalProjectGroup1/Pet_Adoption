from django.urls import path
from .views import (
    HomeView,
    AboutView,
    DonateView,
    MyPetsView,
    AvailableServicesView,
    CreateServiceView,
    AvailableTreatmentsView,
    CreateTreatmentView,
    FindCatsView,
    FindDogsView,
    FindOtherPetsView,
    FindAllView,
    RegisterView,
    AnimalDetailView,
    CreateAdoptionView,
    AdoptionStoriesView,
    UserProfileDetailView,
    UserProfileUpdateView,
    AdoptionPendingListView,
    ApproveAdoptionView,
    AddAdoptionStoryView,
    AnimalFavouriteListView,
    MyAdoptionFormsView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about", AboutView.as_view(), name="about"),
    path("donate", DonateView.as_view(), name="donate"),
    path("animal_detail/<int:animal_id>/",AnimalDetailView.as_view(),name="animal_detail"),
    path("my_pets/", MyPetsView.as_view(), name="my_pets"),
    path('my_adoption_form/', MyAdoptionFormsView.as_view(), name="my_adoption_forms"),
    path("services/<int:pk>/", AvailableServicesView.as_view(), name="services"),
    path("service/create/<int:animal_id>/",CreateServiceView.as_view(),name="create_service"),
    path("treatments/<int:pk>/", AvailableTreatmentsView.as_view(), name="treatments"),
    path("treatment/create/<int:animal_id>/",CreateTreatmentView.as_view(),name="create_treatment"),
    
    path("cats/find", FindCatsView.as_view(), name="find_cats"),
    path("dogs/find", FindDogsView.as_view(), name="find_dogs"),
    path("other_pets/find", FindOtherPetsView.as_view(), name="find_other_pets"),
    path("all_pets/find", FindAllView.as_view(), name="find_all_pets"),
        
    path("adoption/create/", CreateAdoptionView.as_view(), name="create_adoption"),
    path("adoption/pending/", AdoptionPendingListView.as_view(), name="adoption_pending_list"),
    path("adoption/approve/<int:pk>/", ApproveAdoptionView.as_view(), name="approve_adoption"),
    path("adoption/story/add/<int:adoption_pk>/", AddAdoptionStoryView.as_view(), name="add_adoption_story"),
    path("adoption/story", AdoptionStoriesView.as_view(), name="adoption_stories"),

    path('userprofile/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile_detail'),
    path('userprofile/<int:pk>/update', UserProfileUpdateView.as_view(), name='userprofile_update'),
        
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),

    path('favourites/', AnimalFavouriteListView.as_view(), name='animal_favourite_list'),


]
