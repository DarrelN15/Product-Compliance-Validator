from django import forms
from .models import Product, ComplianceStandard

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'dimensions', 'weight', 'material_composition']

class ComplianceStandardForm(forms.ModelForm):
    class Meta:
        model = ComplianceStandard
        fields = ['name', 'description', 'rules']  # Assuming rules is a JSONField for flexible compliance rules
