from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.longin),

    path(r'check_code.html', views.check_code),
]
