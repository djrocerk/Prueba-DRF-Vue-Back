from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Users(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='auth_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='auth_user_set_permissions')
    
    class Meta:
        db_table = 'Usuarios'
    
        