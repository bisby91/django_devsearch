from django.urls import path
from . import views

urlpatterns =[
    path("login-register", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register_user, name="register"),
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>", views.user_profile, name="user-profile")
]