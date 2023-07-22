from django.contrib.auth.models import BaseUserManager
import random 

class UserManager(BaseUserManager):
    def create_user(self, email,user_type="2",otp=None, password=None,**kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type,

        )
       
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None,**kwargs):
        """
        Creates and saves a superuser with the given email,
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.is_superuser=True 
        user.user_type="1"
        user.otp=random.randint(11111,99999)
        user.is_verified=True
        user.save(using=self._db)
        
        return user 


