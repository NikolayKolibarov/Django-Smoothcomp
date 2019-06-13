from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'competitions'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.show, name="show"),
    path('<int:id>/register', views.register, name="register"),
]