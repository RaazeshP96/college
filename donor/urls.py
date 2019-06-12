from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('service/', views.service),
    path('about/', views.about),
    path('donor/', views.donor),
    path('contact/', views.contact),
    path('reciever/', views.reciever),
]