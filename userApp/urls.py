from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addView, name="add"),
    path('view/', views.displayView, name="add"),
]
