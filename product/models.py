from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from .choices import *
# Create your models here.



class Product(models.Model):

    CONDITION_TYPE = (
        ("New" , "New") ,
        ("Used" , "Used")
    )

    ## contain all the products informations
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User , on_delete=models.CASCADE)
    department = models.ForeignKey('Department' , on_delete=models.SET_NULL , null=True)
    description = models.TextField(max_length=500)
    condition = models.CharField(max_length=100 , choices=CONDITION_TYPE)
    
    contact_number = models.CharField(max_length=10 ,  null=True,blank=False)
    original_price = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='main_product/' ,  blank = True,null=True)
    created = models.DateTimeField(default=timezone.now)




    slug = models.SlugField(blank=True  , null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug and self.name :
            self.slug = slugify(self.name)
        super(Product , self).save(*args , **kwargs)


    def __str__(self):
        return self.name



class ProductImages(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to='products/' , blank=True , null=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'






class Category(models.Model):
    ## for product category
    category_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/' , blank=True , null=True)

    slug = models.SlugField(blank=True  , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.category_name :
            self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class Department(models.Model):
    ## for product category
    department_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='department/' , blank=True , null=True)

    slug = models.SlugField(blank=True  , null=True)


    def save(self , *args , **kwargs):
        if not self.slug and self.department_name :
            self.slug = slugify(self.department_name)
        super(Department , self).save(*args , **kwargs)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.department_name







