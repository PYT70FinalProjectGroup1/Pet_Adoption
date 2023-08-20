from django.contrib import admin
from .models import Pet, People


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "species","breed","colour", "chip", "available_for_adoption"]
    list_filter = ["breed","colour","available_for_adoption"]
    search_fields = ["species"]

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ["name", "surname"]
    list_filter = ["id"]
    search_fields = ["surname"]
