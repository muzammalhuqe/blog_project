from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile', on_delete = models.CASCADE,blank=True,null=True)
    image = models.ImageField(upload_to="authentication/images")
    is_admin = models.BooleanField(default=False)



    def __str__(self):
        return f"Username : {self.user.username} , is_admin : {self.is_admin}"

