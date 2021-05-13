from django.shortcuts import render
from .models import Product , ProductImages , Category,Department
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.


def productlist(request , category_slug=None ,department_slug=None):
    category = None
    productlist = Product.objects.all()
    department= None
    categorylist = Category.objects.annotate(total_products=Count('product'))
    departmentlist = Department.objects.annotate(total_products=Count('product'))
    latest_products = Product.objects.order_by("-created")[:3]

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        productlist = productlist.filter(category=category)
    elif department_slug :
        department = get_object_or_404(Department ,slug=department_slug)
        productlist = productlist.filter(department=department)
    
   

    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
           
            Q(category__category_name__icontains = search_query) 
        )

    paginator = Paginator(productlist, 20) # Show 25 contacts per page
    page = request.GET.get('page')
    productlist = paginator.get_page(page)
    template = 'Product/product_list.html'

    context = {'product_list' : productlist , 'category_list' : categorylist ,'category' : category , 'departmentlist' : departmentlist ,'department' : department, 'latest_products':latest_products}
    return render(request , template , context)

# def productlist(request , category_slug=None , department_slug=None):
#     category = None
#     department = None
#     productlist = Product.objects.all()
#     categorylist = Category.objects.annotate(total_products=Count('product'))
#     departmentlist = Department.objects.annotate(total_products=Count('product'))
    

#     if category_slug :
#         category = get_object_or_404(Category ,slug=category_slug)
#         productlist = productlist.filter(category=category)
    
#     if department_slug :
#         department = get_object_or_404(Department ,slug=department_slug)
#         productlist = productlist.filter(department=department)

#     search_query = request.GET.get('q')
#     if search_query :
#         productlist = productlist.filter(
#             Q(name__icontains = search_query) |
#             Q(description__icontains = search_query)|
#             Q(condition__icontains = search_query)|
           
#             Q(category__category_name__icontains = search_query) 
#         )

#     paginator = Paginator(productlist, 20) # Show 25 contacts per page
#     page = request.GET.get('page')
#     productlist = paginator.get_page(page)
#     template = 'Product/product_list.html'

#     context = {'product_list' : productlist , 'category_list' : categorylist ,'category' : category, 'department_list' : departmentlist ,'department' : department }
#     return render(request , template , context)





def productdetail(request , product_slug):
    
    productdetail = Product.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)
    template = 'Product/product_detail.html'
    context = {'product_detail' : productdetail , 'product_images' : productimages}
    return render(request , template , context)



