from django.urls import path, include
from . import api


urlpatterns = [
    #api criação de usuarios
    path('arraiakhrys/signup/api/', api.SignUp.as_view()),
]