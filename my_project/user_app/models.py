from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signup(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField()



class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField()


class Blog(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)