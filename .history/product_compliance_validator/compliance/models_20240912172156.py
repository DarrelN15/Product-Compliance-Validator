from django.db import models

# Create your models here.

class ComplianceStandard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ComplianceResult(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    standard = models.ForeignKey(ComplianceStandard, on_delete=models.CASCADE)
    is_compliant = models.BooleanField(default=False)
    details = models.TextField(blank=True, null=True)  # Stores details on why the product is non-compliant
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} vs {self.standard.name} - {'Compliant' if self.is_compliant else 'Non-Compliant'}"