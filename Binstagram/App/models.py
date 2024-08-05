from django.db import models

# Create your models here.
class siteuser(models.Model):
    Username=models.CharField(max_length =255)
    Password=models.CharField(max_length =255)
