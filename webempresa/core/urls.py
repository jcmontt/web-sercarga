from django.urls import path
from . import views

urlpatterns = [
    #paths del core
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),
    path('storte/', views.store, name='store'),
]