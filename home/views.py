from django.shortcuts import render
from product.models import Product , Category,Department
# Create your views here.

def home(request):
    
    all_category = Category.objects.all() 
    all_department = Department.objects.all() 
    
    products = Product.objects.all()
    latest_products = Product.objects.order_by("-created")[:4]
    template = 'home.html'
    context = { 'all_category' : all_category  ,'products' : products, 'all_department':all_department, 'latest_products' :latest_products}

    return render(request , template , context)