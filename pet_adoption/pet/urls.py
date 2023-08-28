from django.urls import path
from pet.views import (
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
    AnimalDetailView,
    CreateAdoptionView,
    AdoptionStoriesView,
    AdoptionPendingListView,
    ApproveAdoptionView,
    AddAdoptionStoryView,
    AnimalFavouriteListView,
    MyAdoptionFormsView,
    AnimalSearchView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("donate/", DonateView.as_view(), name="donate"),
    path("about/", AboutView.as_view(), name="about"),
    path("animal_search/", AnimalSearchView.as_view(), name="animal_search"),
    path(
        "animal_detail/<int:animal_id>/",
        AnimalDetailView.as_view(),
        name="animal_detail",
    ),
    path("my_pets/", MyPetsView.as_view(), name="my_pets"),
    path("my_adoption_forms/", MyAdoptionFormsView.as_view(), name="my_adoption_forms"),
    path("services/<int:pk>/", AvailableServicesView.as_view(), name="services"),
    path(
        "services/create/<int:animal_id>/",
        CreateServiceView.as_view(),
        name="create_service",
    ),
    path("treatments/<int:pk>/", AvailableTreatmentsView.as_view(), name="treatments"),
    path(
        "treatments/create/<int:animal_id>/",
        CreateTreatmentView.as_view(),
        name="create_treatment",
    ),
    path("cats/find/", FindCatsView.as_view(), name="find_cats"),
    path("dogs/find/", FindDogsView.as_view(), name="find_dogs"),
    path("other_pets/find/", FindOtherPetsView.as_view(), name="find_other_pets"),
    path("all_pets/find/", FindAllView.as_view(), name="find_all_pets"),
    path("adoption/create/", CreateAdoptionView.as_view(), name="create_adoption"),
    path(
        "adoption/pending/",
        AdoptionPendingListView.as_view(),
        name="adoption_pending_list",
    ),
    path(
        "adoption/<int:pk>/approve/",
        ApproveAdoptionView.as_view(),
        name="approve_adoption",
    ),
    path(
        "adoption/story/<int:adoption_pk>/add/",
        AddAdoptionStoryView.as_view(),
        name="add_adoption_story",
    ),
    path("adoption/stories/", AdoptionStoriesView.as_view(), name="adoption_stories"),
    path(
        "favourites/", AnimalFavouriteListView.as_view(), name="animal_favourite_list"
    ),
]
