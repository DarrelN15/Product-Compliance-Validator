from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ComplianceStandard, Product, ComplianceResult

admin.site.register(ComplianceStandard)
admin.site.register(Product)
admin.site.register(ComplianceResult)
