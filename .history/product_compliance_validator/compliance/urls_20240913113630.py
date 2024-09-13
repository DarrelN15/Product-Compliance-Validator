# compliance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check_compliance, name='check_compliance'),  # Compliance check view
    path('add-product/', views.add_product, name='add_product'),
    path('add-standard/', views.add_standard, name='add_standard'),
]
