from django.shortcuts import redirect, render, get_object_or_404
from .forms import UserForm , UserProfileForm
from .models import user_profile
from django.contrib.auth import authenticate, login
from product.models import Product
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('/products')

    else:
        user_form = UserForm()
        profile_form = UserProfileForm( )
    context = {'user_form' : user_form,
              'profile_form': profile_form}

    return render(request , 'registration/register.html' , context)



def profile_detail(request):
    # profile = user_profile.objects.get(user=request.user)
    ad_list = Product.objects.filter(owner = request.user)
    profile =None
    
    
    return render(request,'accounts/profile.html',{'profile': profile,  'ad_list':ad_list})


# def profile_edit(request):
#     profile = Profile.objects.get(user=request.user)
#     if request.method=='POST':
#         userform = UserEditForm(request.POST , instance=request.user)
#         profileform = ProfileEditForm(request.POST , instance=profile)
        
#         if userform.is_valid() and profileform.is_valid():
#             userform.save()
#             myform = profileform.save(commit=False)
#             myform.user = request.user
#             myform.save()
           
#             return redirect('/accounts/profile')

#     else:
#         userform = UserEditForm(instance=request.user)
#         profileform = ProfileEditForm(instance=profile)

#     return render(request,'accounts/edit_profile.html',{
#         'userform' : userform,
#         'edit_profile' : profileform
#     })

def product_delete(request , pk):
    product = get_object_or_404(Product , pk = pk)

    if request.method== 'POST':
        product.delete()
        return redirect('/')
    
    return render(request,'accounts/profile.html' )


    