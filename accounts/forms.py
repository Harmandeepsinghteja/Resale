from django import forms
from django.contrib.auth.models import User
from .models import user_profile

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name' , 'last_name' ,'username' , 'email' , 'password' ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = user_profile
        fields = ['phone_number']


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email']


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['phone_number']


