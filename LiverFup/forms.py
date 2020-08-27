from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


from .models import inrollment,Visit


class inrollmentForm(forms.ModelForm):

    National_ID =forms.CharField(max_length=14,validators=[RegexValidator('(2|3)[0-9][1-9][0-1][1-9][0-3][1-9](01|02|03|04|11|12|13|14|15|16|17|18|19|21|22|23|24|25|26|27|28|29|31|32|33|34|35|88)\d\d\d\d\d',message="please enter avalid national ID")],widget=forms.NumberInput( attrs={ 'class':"form-control"}))


    age = forms.IntegerField(max_value=100,min_value=18 ,widget=forms.NumberInput( attrs={ 'class':"form-control"}))

    class Meta:

       model = inrollment
       fields = ('patient_name','National_ID','age','Center_ID','gender','Comorbidities','Cause_of_Liver_Cirrhosis',
       'HCV_Treatmen_If_not_Pick_Na','In_case_OF_HCV_OutCome')

       widgets = {
               'patient_name':forms.TextInput(attrs={ 'class':"form-control"}),
              'gender':forms.Select(attrs={ 'class':"form-control"}),
              'Center_ID':forms.TextInput(attrs={ 'class':"form-control",'value':'','id':'emji','type':'hidden'}),
              'Comorbidities' :forms.Select(attrs={ 'class':"form-control"}),
              'Cause_of_Liver_Cirrhosis':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_Treatmen_If_not_Pick_Na':forms.Select(attrs={ 'class':"form-control"}),
              'In_case_OF_HCV_OutCome':forms.Select(attrs={ 'class':"form-control"}),

          }
