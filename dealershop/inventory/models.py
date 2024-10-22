from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.IntegerField(default=1900)

class Inventory(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    number = models.IntegerField(default=1900)

    