from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Ensure these fields exist (override if needed)
    email = models.EmailField(unique=True, blank=False)
    
    # Add any custom fields
    # profile_picture = models.ImageField(upload_to='profiles/', null=True)
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'