from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Standard, Product, ComplianceResult

admin.site.register(Standard)
admin.site.register(Product)
admin.site.register(ComplianceResult)
