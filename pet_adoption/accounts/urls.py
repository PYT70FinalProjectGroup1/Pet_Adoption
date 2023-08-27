from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    RegisterView,
    UserProfileDetailView,
    UserProfileUpdateView,
)

app_name = "accounts"

urlpatterns = [
    path(
        "userprofile/<int:pk>/",
        UserProfileDetailView.as_view(),
        name="userprofile_detail",
    ),
    path(
        "userprofile/<int:pk>/update/",
        UserProfileUpdateView.as_view(),
        name="userprofile_update",
    ),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
]
