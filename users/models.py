from django.db import models 
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.utils.html import format_html
from django.core.exceptions import ValidationError
 
#
 
class User(AbstractBaseUser):
    full_name=models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        unique=True
       
    ) 
    user_type=models.CharField(max_length=1,choices=(
        ("1","Administrator"),
        ("2","Blogger"),
        
         )
         ,default="2")
    profile_avatar=models.ImageField(upload_to="media/profile",default="media/default/profile_avatar.png")
    otp=models.PositiveBigIntegerField(blank=True,null=True)
   
    
    is_active = models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_disabled=models.BooleanField(default=False) 
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin 

    def profile_avatar_circle(self):
        return format_html(f"<img src='{self.profile_avatar.url}' style='width:25px;border-radius:50%'>")


    class Meta:
        db_table="users"
    
   


class Contact(models.Model):
    author=models.OneToOneField(User,on_delete=models.CASCADE) 
    address=models.TextField()
    phone=models.CharField(max_length=255) 
    email=models.EmailField()
    facebook_link=models.URLField() 
    facebook_follower=models.CharField(max_length=20)
    twitter_link=models.URLField() 
    twitter_follower=models.CharField(max_length=20) 
    linkedin_link=models.URLField() 
    linkedin_follower=models.CharField(max_length=20)  

    def __str__(self) -> str:
        return self.author.full_name
    


class Subsciber(models.Model):
    email=models.EmailField(unique=True) 
    def __str__(self) -> str:
        return self.email 


