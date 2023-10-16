from django.db import models
from django.contrib import auth

# Create your models here.
class NameCon(models.Model):
    name_con = models.CharField(max_length=12)

class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=15)

class PinNumber(models.Model):
    pin_number = models.IntegerField()

class RowNumber(models.Model):
    row_number = models.IntegerField()

class TypeCon(models.Model):
    type_con = models.CharField(max_length=15)

class Connector(models.Model):
    part_number = models.CharField(max_length=10)
    customer_number = models.CharField(max_length=15)
    name_con = models.ForeignKey(NameCon, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pin_number = models.ForeignKey(PinNumber, on_delete=models.CASCADE)
    row_number = models.ForeignKey(RowNumber, on_delete=models.CASCADE)
    type_con = models.ForeignKey(TypeCon, on_delete=models.CASCADE)




