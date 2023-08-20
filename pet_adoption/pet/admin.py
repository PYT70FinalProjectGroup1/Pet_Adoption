from django.contrib import admin
from .models import Animal, UserProfile, Adoption, Treatments, Services

admin.site.register(UserProfile)
admin.site.register(Animal)
admin.site.register(Adoption)
admin.site.register(Treatments)
admin.site.register(Services)
