# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .manager import *

# class CustomUser(AbstractUser):
    
#     username = None
#     phone_number = models.CharField(max_length=100, unique=True)
#     first_name = models.CharField(max_length=100, unique=True, null = True, blank = True)
#     last_name = models.CharField(max_length=100, unique=True, null = True, blank = True)
#     email = models.EmailField(unique=True, null = True, blank = True)
#     user_bio = models.CharField(max_length=50, null = True, blank = True)
#     user_profile_image = models.ImageField(upload_to='profile', null = True, blank = True)
    
    
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#     objects  = UserManager()