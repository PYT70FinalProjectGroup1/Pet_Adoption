from django.contrib import admin
from .models import Animal, UserProfile, Adoption, Treatment, Service


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "species","breed","colour", "chip", "available_to_adoption"]
    list_filter = ["breed","colour","available_to_adoption"]
    search_fields = ["species"]



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    list_filter = ["id"]
    search_fields = ["surname"]


admin.site.register(Adoption)
admin.site.register(Treatment)
admin.site.register(Service)
