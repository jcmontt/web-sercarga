from django.urls import path
from . import views

urlpatterns = [
    #paths del core
    path('', views.services, name='services'),
]