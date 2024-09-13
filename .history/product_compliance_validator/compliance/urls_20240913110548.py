# compliance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check_compliance, name='check_compliance'),  # Compliance check view
]
