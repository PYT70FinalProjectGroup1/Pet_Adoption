from django.urls import path
from .views import AdoptionListView, AnimalListView, UserProfileListView

urlpatterns = [
    path('animals/', AnimalListView.as_view(), name='animals'),

]