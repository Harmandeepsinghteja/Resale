from django import forms
from product.models import Product,ProductImages

class post_ad_form(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [ 'owner','created' , 'slug' ]



class images_form(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = ProductImages
        fields = [ 'image' ]


