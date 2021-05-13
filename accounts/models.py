from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class user_profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=25 ,  null=True,blank=False,unique=True)



    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            user_profile.objects.create(user=instance)
        instance.user_profile.save()        

    

