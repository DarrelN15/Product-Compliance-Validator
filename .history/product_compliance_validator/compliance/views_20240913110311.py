from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Product, ComplianceStandard, ComplianceResult
from .services import ComplianceCheckEngine

# View to check compliance for a product against a standard
def check_compliance(request):
    if request.method == "POST":
        # Get selected product and standard from the form
        product_id = request.POST.get("product")
        standard_id = request.POST.get("standard")

        product = get_object_or_404(Product, pk=product_id)
        standard = get_object_or_404(ComplianceStandard, pk=standard_id)

        # Run the compliance check engine
        engine = ComplianceCheckEngine(product=product, standard=standard)
        is_compliant, compliance_message = engine.check_compliance()

        # Save the result to the database
        result = ComplianceResult.objects.create(
            product=product,
            standard=standard,
            is_compliant=is_compliant,
            details=compliance_message if not is_compliant else "Product is fully compliant."
        )

        # Pass the result to the template to display it
        context = {
            "product": product,
            "standard": standard,
            "is_compliant": is_compliant,
            "compliance_message": compliance_message,
        }
        return render(request, "compliance/compliance_result.html", context)

    # If GET request, show the form to select product and standard
    products = Product.objects.all()
    standards = ComplianceStandard.objects.all()
    context = {
        "products": products,
        "standards": standards,
    }
    return render(request, "compliance/check_compliance.html", context)
