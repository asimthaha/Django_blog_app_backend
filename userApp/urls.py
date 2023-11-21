from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.registerView, name="add"),
    path('view/', views.displayUserView, name="view"),
    path('loginCheck/', views.LoginView, name="logincheck"),
    path('updateView/', views.LoginView, name="updateView"),
]
