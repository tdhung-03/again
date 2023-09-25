from django.urls import path
from .views import *
urlpatterns = [
    path("profile/<int:id>", profile, name="profile"),
    path("register/", create_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]