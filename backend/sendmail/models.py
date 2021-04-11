from django.db import models

# Create your models here.

class Mail(models.Model):
    name = models.CharField(max_length=100)
    
    creation_date = models.DateTimeField()
    country = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    city_key = models.IntegerField()
    street = models.CharField(max_length= 100)
    street_number = models.CharField(max_length=10)



