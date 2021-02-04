from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from product.models import Product, ProductImages
from .forms import post_ad_form,images_form


from django.forms.models import modelformset_factory


@login_required
def post_ad_view(request):
    ImageFormSet = modelformset_factory(ProductImages,
                                        form=images_form,extra=2)
    if request.method == "POST":
        ad_form = post_ad_form(request.POST , request.FILES )
        form_set = ImageFormSet(request.POST, request.FILES,
                               queryset=ProductImages.objects.none())
        
        if ad_form.is_valid() and form_set.is_valid():
            
            ad_form = ad_form.save(commit=False)
            ad_form.owner = request.user
            ad_form.save()
            
            
            form_set.save(commit=False)
            for form in form_set.cleaned_data:
                image = form['image']
                
                photo = ProductImages(product=ad_form, image=image)
                photo.save()


                
            
            return redirect('/')
            
            
    
        
    else:
        ad_form = post_ad_form()
        form_set = ImageFormSet(queryset=ProductImages.objects.none())
        
    return render(request, "ad/post-ad.html", {'form':ad_form, 'image_form':form_set })


