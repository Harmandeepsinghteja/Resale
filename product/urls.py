from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('' , views.productlist , name='product_list') , 
    path('category/<slug:category_slug>' , views.productlist , name='product_list_category') , 
    path('department/<slug:department_slug>' , views.productlist , name='product_list_department') , 
    
    path('detail/<slug:product_slug>' , views.productdetail , name='product_detail'),
    
]