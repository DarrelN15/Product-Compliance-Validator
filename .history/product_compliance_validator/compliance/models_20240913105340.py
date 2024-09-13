from django.db import models

# Create your models here.

from django.db import models
import jsonfield

class ComplianceStandard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Store rules dynamically, so you can define thresholds for various attributes like weight, dimensions, etc.
    rules = jsonfield.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


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
    
class ComplianceCheckEngine:
    def __init__(self, product, standard):
        self.product = product
        self.standard = standard
        self.non_compliance_reasons = []

    def check_compliance(self):
        # Iterate through all rules in the standard and apply them dynamically
        for attribute, rule in self.standard.rules.items():
            product_value = getattr(self.product, attribute, None)
            if product_value is not None:
                self.apply_rule(attribute, product_value, rule)
            else:
                self.non_compliance_reasons.append(f"{attribute} is missing from the product data.")
        
        if not self.non_compliance_reasons:
            return True, "Product is fully compliant."
        else:
            return False, self.non_compliance_reasons

    def apply_rule(self, attribute, product_value, rule):
        # Check based on the type of rule (e.g., range, allowed values)
        if "min" in rule and product_value < rule["min"]:
            self.non_compliance_reasons.append(
                f"{attribute} is below the minimum allowed value. {product_value} < {rule['min']}"
            )
        if "max" in rule and product_value > rule["max"]:
            self.non_compliance_reasons.append(
                f"{attribute} exceeds the maximum allowed value. {product_value} > {rule['max']}"
            )
        if "allowed" in rule and product_value not in rule["allowed"]:
            self.non_compliance_reasons.append(
                f"{attribute} has an invalid value. {product_value} is not in {rule['allowed']}"
            )
