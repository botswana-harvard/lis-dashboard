from django.conf import settings
from django.urls.conf import path, include
from edc_dashboard import UrlConfig

requisition_identifier = ''
from .views import RequisitionListboardView

app_name = 'lis_dashboard'

sample_reception_listboard_url_config = UrlConfig(
    url_name='sample_reception_listboard_url',
    view_class=RequisitionListboardView,
    label='lis_listboard',
    identifier_label='requisition_identifier',
    identifier_pattern=requisition_identifier)

urlpatterns = []
urlpatterns += sample_reception_listboard_url_config.listboard_urls

if settings.APP_NAME == 'lis_dashboard':

    from django.views.generic.base import RedirectView

    urlpatterns += [
        path('edc_device/', include('edc_device.urls')),
        path('edc_protocol/', include('edc_protocol.urls')),
        path('admininistration/', RedirectView.as_view(url='admin/'),
             name='administration_url'),
        path('accounts/', include('edc_base.auth.urls')),
        path('admin/', include('edc_base.auth.urls')),
        path('edc_lab/', include('edc_lab.urls')),
        path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
        path(r'', RedirectView.as_view(url='admin/'), name='home_url')]
