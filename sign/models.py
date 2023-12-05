from django.db import models

# Create your models here.
class Sign(models.Model):
  username = models.CharField(max_length=50,default=None)
  password = models.CharField(max_length=50,default=None)
  
  
    