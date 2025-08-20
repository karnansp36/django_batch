from django.db import models

# Create your models here.
class User_db(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class image_storage(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    files = models.FileField(upload_to='files/', blank=True, null=True )