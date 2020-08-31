from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout",views.logout, name="logout"),
    path("details", views.details, name="details"),
    path("register", views.register, name="register"),
    path("registered", views.registered, name="registered"),
    path("index", views.index, name="index"),
    path("event",views.event,name="event"),
     ]

