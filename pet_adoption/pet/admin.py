from django.contrib import admin
from .models import Animal, UserProfile, Adoption, Treatment, Service


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


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_filter = ["id"]
    search_fields = ["surname"]


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
