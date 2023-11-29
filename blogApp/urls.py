from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addView, name="add"),
    path('search/', views.searchView, name="search"),
    path('view/', views.displayView, name="view"),
    path('viewMy/', views.displayMyView, name="viewMy"),
    path('deleteMy/', views.deleteView, name="deleteMy"),
    path('updateMy/', views.updateView, name="updateMy"),
    path('displayUpdateMy/', views.displayUpdateView, name="displayUpdateMy"),   
]
