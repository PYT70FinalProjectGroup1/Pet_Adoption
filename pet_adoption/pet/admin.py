from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Animal, Adoption, Treatment, Service, Location, AdoptionStory


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "species",
        "breed",
        "color",
        "gender",
        "size",
        "age",
        "chip",
        "location",
        "is_available_for_adoption",
    ]
    list_filter = ["breed", "color", "is_available_for_adoption", "age", "size"]
    search_fields = ["species"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city_key", "city_name"]
    list_filter = ["city_key"]
    search_fields = ["city_name"]


@admin.register(Adoption)
class AdoptionAdmin(admin.ModelAdmin):
    list_display = ["user", "animal", "is_approved"]
    list_filter = ["animal"]
    search_fields = ["animal"]


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ["animal", "treatment_name", "created_at"]
    list_filter = ["animal"]
    search_fields = ["animal"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["animal", "service_name", "price"]
    list_filter = ["animal"]
    search_fields = ["animal"]


@admin.register(AdoptionStory)
class AdoptionStoryAdmin(admin.ModelAdmin):
    list_display = ["story_title"]
    list_filter = ["story_title"]
    search_fields = ["story_title"]
