from django.contrib import admin
from django import forms
from django.contrib.admin.options import InlineModelAdmin

# from .models import NameCon

from connectordb.models import Connector, ConnectorName, Manufacturer, Using, TypeCon, PinNumber, RowNumber


class ConnectorAdmin(admin.ModelAdmin):
    list_display = ("part_number", "customer_number", "connector_name", "using", "manufacturer",)




# Register your models here.
admin.site.register(Connector, ConnectorAdmin)
admin.site.register(Manufacturer)   # pridá se do CONECTORDB jako další položka, tu vyplním údaji a ty se zpřístupní při zadávání connectoru
admin.site.register(ConnectorName)
admin.site.register(Using)
admin.site.register(TypeCon)
admin.site.register(PinNumber)
admin.site.register(RowNumber)


