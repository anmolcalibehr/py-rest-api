from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Manager for UserProfiles """ 

def create_user(self, email , name , password=None):
    """ Create a New User Profile """
    if not email:
        raise ValueError('User Must Enter an Email Address')

    email = self.normalize_email(email)
    user  = self.model(email=email, name=name)

    user.set_password(password)
    user.save(using=self._db)
 
    return user

def create_superuser(self , email , name , password):
    """ Create a New Super User with Fewer Details"""
    user = self.create_user(email, name , password)

    user.is_superuser = True 
    user.is_staff = True
    user.save(using=self._db)

    return user


class UserProfile(AbstractBaseUser , PermissionsMixin):
    """ Database Models For User """
    email = models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

def get_full_name(self):
    """ Retrieve Full Name Of User """
    return self.name

def get_short_name(self):
    """ Retrieve Short Name of User """
    return self.name

def __str__(self):
    """ Return String Representation of Our User """    
    return self.email


