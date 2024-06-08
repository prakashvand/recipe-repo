from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy  as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class User(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField(max_length =200,null=True,blank=True,default='')
    last_name = models.CharField(max_length =200,null=True,blank=True,default ='')
    username = models.CharField(null=True, blank=True, default='', max_length=50)
    email = models.CharField(max_length =200,null=True,blank=True,default ='')
    mobile = models.CharField(_('Contact phone number'),max_length=13, unique=True)
    dob = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=20, blank=True, choices=GENDER, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    base_url = models.CharField(max_length =7,unique =True,null=True,blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_account_management_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_account_management_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return str(full_name.strip()) +' - '+ str(self.mobile)

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_user_token(self):
        token = Token.objects.get(user = self).key
        if token:
            return token
        else:
            return False
        
# @receiver(post_save, sender=User)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
   
        

        
