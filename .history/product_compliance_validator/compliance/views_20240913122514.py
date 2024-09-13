from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ComplianceStandard, ComplianceResult
from .services import ComplianceCheckEngine
from .forms import ComplianceStandardForm, ProductForm

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


# View to manage compliance standards
"""
View to manage compliance standards.

This view allows users to add new products to the system. It uses a form to capture the product details.

Parameters:
- request: The HTTP request object. It contains information about the client and the requested page.

Returns:
- If the request method is POST, the function validates the form data, saves the new product to the database,
  and redirects the user to the 'add_products' page.
- If the request method is GET, the function renders the 'compliance/add_product.html' template with an empty form.
"""
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list") # Redirect to a product list or some other view
    else:
        form = ProductForm()
    return render(request, "compliance/add_product.html", {"form": form})

# View to add a new compliance standard
def add_standard(request):
    if request.method == "POST":
        form = ComplianceStandardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("standard_list") # Redirect to a standard list or some other view
    else:
        form = ComplianceStandardForm()
    return render(request, "compliance/add_standard.html", {"form": form}) 

# List of products
def product_list(request):
    products = Product.objects.all()
    return render(request, "compliance/product_list.html", {"products": products})

# List of compliance standards
def standard_list(request):
    standards = ComplianceStandard.objects.all()
    return render(request, "compliance/standard_list.html", {"standards": standards})

# View to display the compliance result
def compliance_result(request):
    # You can adjust this to show compliance results
    return render(request, 'compliance/compliance_result.html')