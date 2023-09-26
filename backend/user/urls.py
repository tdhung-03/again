from django.urls import path
from .views import profile, create_user, login_user, logout_user, account
urlpatterns = [
    path("profile/<int:id>", profile, name="profile"),
    path("register/", create_user, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("account/", account, name="account"),
]
