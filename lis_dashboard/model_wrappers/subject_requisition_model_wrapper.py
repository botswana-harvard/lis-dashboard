from django.conf import settings
from edc_model_wrapper import ModelWrapper


class SubjectRequisitionModelWrapper(ModelWrapper):

    model = 'sample_reception.subjectrequisition'
    next_url_attrs = ['requsition_identifier']
    next_url_name = settings.DASHBOARD_URL_NAMES.get('sample_reception_listboard_url')
