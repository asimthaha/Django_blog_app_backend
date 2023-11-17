from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addView, name="add"),
    path('search/', views.searchView, name="search"),
    path('view/', views.displayView, name="view"),
]
