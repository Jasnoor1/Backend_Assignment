from django.db import models

# Create your models here.

class Employee(models.Model):
    #id = models.IntegerField()
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField (max_length= 50)
    company_name = models.CharField(max_length= 250)
    age = models.IntegerField()
    city = models.CharField(max_length= 100)
    state = models.CharField(max_length=10)
    zip = models.IntegerField()
    email = models.EmailField(max_length=250)
    web = models.CharField(max_length=250)
