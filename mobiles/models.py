from django.db import models

# Create your models here.
class Mobiles(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField(blank=True)
    price= models.DecimalField(max_digits=5,decimal_places=2)
    image=models.ImageField(upload_to ='photos/%y/%m/%d',default='photos/1.jpg')
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='Mobile'