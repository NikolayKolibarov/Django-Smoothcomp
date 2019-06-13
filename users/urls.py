from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name="register"),
    path('store', views.store, name="store"),
    path('login', views.signinPage, name="login"),
    path('authenticate', views.signin, name="authenticate"),
    path('logout', views.signout, name="logout"),
    path('profile', views.profile, name="profile"),
]