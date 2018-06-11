from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


no_url_namespace = True if settings.APP_NAME == 'lis_dashboard' else False

lis_dashboard = Navbar(name='lis_dashboard')

lis_dashboard.append_item(
    NavbarItem(
        name='sample_reception',
        title='SampleReception',
        label='reception',
        fa_icon='fa fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES['sample_reception_listboard_url'],
        no_url_namespace=no_url_namespace))

site_navbars.register(lis_dashboard)
