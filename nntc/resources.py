from import_export import resources
from nntc.models import Patient ,W0



class PatientResource(resources.ModelResource):

    class Meta:
        model = Patient
        skip_unchanged = True
        report_skipped = True
        import_id_fields =['National_ID']

class w0Resource(resources.ModelResource):
    class Meta:
        model = W0
        skip_unchanged = True
        report_skipped = True
        import_id_fields =['patient']


        
