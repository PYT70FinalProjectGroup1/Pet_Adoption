from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.
@admin.register(get_user_model())
class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "location",
        "profile_picture",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = ["username"]
    search_fields = ["username"]
