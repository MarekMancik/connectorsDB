from django.contrib.admin.apps import AdminConfig


class ConnectordbAdminConfig(AdminConfig):
    default_site = "admin.ConnectorManagementApp"