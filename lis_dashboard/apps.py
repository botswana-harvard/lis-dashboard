from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'lis_dashboard'
    admin_site_name = 'lis_test_admin'
    include_in_administration_section = False
