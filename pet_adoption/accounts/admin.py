from django.contrib import admin
from django.contrib.auth import get_user_model


# Register your models here.
@admin.register(get_user_model())
class UserModelAdmin(admin.ModelAdmin):
    pass