# compliance/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('add_standard/', views.add_standard, name='add_standard'),
    path('check_compliance/', views.check_compliance, name='check_compliance'),
    path('product_list/', views.product_list, name='product_list'), 
    path('standard_list/', views.standard_list, name='standard_list'), 
    path('compliance_result/', views.compliance_result, name='compliance_result'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_standard/<int:standard_id>/', views.edit_standard, name='edit_standard'),
    path('delete_standard/<int:standard_id>/', views.delete_standard, name='delete_standard'),
]
