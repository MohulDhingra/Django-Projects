from django.db import models

# Create your models here.
class item(models.Model):
    Title=models.CharField(max_length =255)
    Description=models.CharField(max_length =255)
    City=models.CharField(max_length =255)
    Price=models.IntegerField()
    img=models.TextField()