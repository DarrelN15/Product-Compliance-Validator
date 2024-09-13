# compliance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('add_standard/', views.add_standard, name='add_standard'),
    path('check_compliance/', views.check_compliance, name='check_compliance'),
]