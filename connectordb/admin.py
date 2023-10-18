from django.contrib import admin

from connectordb.models import Connector

class ConnectorAdmin(admin.ModelAdmin):
    list_display = ("part_number", "customer_number", "connector_name", "using", "manufacturer",)


# Register your models here.
admin.site.register(Connector)