from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

urlpatterns = [
    path('add_animal', views.AddAnimal.as_view({'post': 'post'})),
    path('signup', views.UserSignUp.as_view({'post': 'signup'})),
    path('signin', views.UserSignIn.as_view({'post': 'signin'})),
    # path('add_profile/', views.Avatar.as_view({'post': 'add_profile'}), name='add_profile'),
]
