from django.db import models
from django.contrib import auth

# Create your models here.
class ConnectorName(models.Model):
    CONNECTOR_NAME = [
        ("Plug Housing", "Plug Housing"),
        ("Socked Housing", "Socked Housing"),
    ]

    connector_name = models.CharField(max_length=50, choices=CONNECTOR_NAME)

    def __str__(self):
        return f"{self.connector_name}"   #bez metody __str__() se v tabulkách hodnoty nezobrazí jménem


class Manufacturer(models.Model):
    manufacturer = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.manufacturer}"

class Using(models.Model):
    USING = [
        ("Wire Harness", "Wire Harness"),
        ("PCB", "PCB"),
    ]

    using = models.CharField(max_length=20, choices=USING)

    def __str__(self):
        return f"{self.using}"


class PinNumber(models.Model):
    pin_number = models.IntegerField()

    def __str__(self):
        return f"{self.pin_number}"

class RowNumber(models.Model):
    row_number = models.IntegerField(choices=((1, "1"), (2, "2"), (3, "3")))

    def __str__(self):
        return f"{self.row_number}"

class TypeCon(models.Model):
    type_con = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.type_con}"

class Connector(models.Model):
    part_number = models.CharField(primary_key=True, max_length=10)
    customer_number = models.CharField(max_length=15)
    connector_name = models.ForeignKey(ConnectorName, on_delete=models.CASCADE)
    using = models.ForeignKey(Using, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    pin_number = models.ForeignKey(PinNumber, on_delete=models.CASCADE)
    row_number = models.ForeignKey(RowNumber, on_delete=models.CASCADE)
    type_con = models.ForeignKey(TypeCon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.connector_name}, {self.using}, {self.manufacturer}"


