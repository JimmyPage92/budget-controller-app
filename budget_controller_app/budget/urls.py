from . import views
from django.urls import path

urlpatterns = [
    path('budget-controller/', views.home, name='home-page'),
    path('about/', views.about, name='about-page'),
]