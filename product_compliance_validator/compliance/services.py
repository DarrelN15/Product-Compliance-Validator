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
