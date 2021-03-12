from django.urls import path , include
from . views import register
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/' , register , name='register') , 
    path('profile/',views.profile_detail , name='profile'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('profile/ads',views.profile_ad_detail , name='profile_ad'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    # path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') , 
    # path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
    # path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
    # path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') , 
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']

]