from django.urls import path
from . import views


app_name = 'ad'

urlpatterns = [
    path('' , views.post_ad_view , name='post_ad') , 
    ]