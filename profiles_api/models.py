from django.db import models
# default user model used below for customization
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
#import default manager model that comes with django
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Uses must have email address')

        # normalize email
        email = self.normalize_email(email)
        #create a user model
        #it creates a new model that a user manager representing
        #self.model is set for model the manager is for
        #set email and name
        user = self.model(email=email, name=name)

        #set password is part of AbstractBase User
        #reason we do it the password is encrypted and make sure the
        #password is converted to a hash and never stored in the database
        #with set password function django encrypts a password
        user.set_password(password)
        #specify a databse to use. Django can support multiple databases
        #add the line inside of bracket to make sure that you support multiple
        #database
        user.save(using = self._db)

        return user

        # super use has admin user status
    def create_superuser(self, email, name, password):
        """Create superuser function"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique = True)
    name = models.CharField(max_length=255)
    # the next ones for permission system
    #to determine whether user_profile is activated or not
    is_active = models.BooleanField(default=True)
    # determine whether a user is staff use.
    #it determines whether use should have an access to admin like that
    is_staff = models.BooleanField(default=False)

    #specify model manager to use for object - user profile manager
    objects = UserProfileManager()
    #inside of above brackets we will put class
    # we also need add a couple more fields to work with django admin
    #and django authentication system
    #overriding the default user_name field with email

    USERNAME_FIELD = 'email'
    #additional requirement apart from default email specified below
    REQUIRED_FIELDS = ['name']

    #add couple of functions to interact with our custom user model
    #retrieve full user name function
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    #specify get short name

    def get_short_name(self):
        """Get short name of user"""
        return self.name

    #string representation of our model. this is the item we want to return
    #when we convert a user profile object to a string in Python

    def __str__(self):
        """Return string representation of our user"""
        return self.email
