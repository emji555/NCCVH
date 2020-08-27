from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.
class inrollment(models.Model):
    patient_name =models.CharField(max_length=200,null=False)
    National_ID =models.CharField( max_length=14,null=False,unique=True)
    Center_ID=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(null=False)
    Gender_choices=(
        ('Male','Male'),
        ('Female','Female'),
    )
    gender=models.CharField(choices=Gender_choices, max_length=300,null=True,blank=True)



    Comorbidities_choise =(
        ('No Comorbidities','No Comorbidities'),
        ('Cardiac','Cardiac'),
        ('Chest','Chest'),
        ('Renal','Renal'),
        ('Other','Other'),

    )
    Comorbidities = models.CharField(choices=Comorbidities_choise,max_length=50,null=True,blank=True)

    Cause_of_Liver_Cirrhosis_choise= (
        ('HCV','HCV'),
        ('HBV','HBV'),
        ('Other Cuses','Other Cuses'),



    )
    Cause_of_Liver_Cirrhosis=models.CharField(choices=Cause_of_Liver_Cirrhosis_choise,max_length=20,null=True,blank=True)

    in_case_HCV_choise = (
        ('SOF/DAC','SOF/DAC'),
        ('SOF/DAC/RBV','SOF/DAC/RBV'),
        ('PAR/OMB','PAR/OMB'),
        ('PAR/OMB/RBV','PAR/OMB/RBV'),
        ('SOF/DAC/SIM','SOF/DAC/SIM'),
        ('SOF/PAR/OMB/RBV','SOF/PAR/OMB/RBV'),
        ('SOF/LED','SOF/LED'),
        ('IFN/RBV','IFN/RBV'),
        ('SOF/INF/RBV','SOF/INF/RBV'),
        ('SOF/RBV','SOF/RBV'),
        ('SOF/SIM','SOF/SIM'),
        ('SOF/DAC/SIM/RBV','SOF/DAC/SIM/RBV'),
        ('N/A','N/A'),




     )



    HCV_Treatmen_If_not_Pick_Na = models.CharField(
       choices=in_case_HCV_choise
       ,max_length=50,null=True,blank=True)


    in_case_HCV_Out_come_choise = (
        ('Responder','Responder'),
        ('Relapser','Relapser'),
        ('N/A','N/A'),
    )

    In_case_OF_HCV_OutCome = models.CharField(choices=in_case_HCV_Out_come_choise,max_length=50,null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.patient_name
    def get_absolute_url(self):
            return reverse ('LiverList')








class Visit(models.Model):
    class Meta:
        unique_together = (('inrollment_id','visit_num'),)

    inrollment_id = models.ForeignKey(inrollment,on_delete=models.CASCADE,related_name='visits')
    visit_num = models.IntegerField(null=False)
    AFP = models.DecimalField(null=True,decimal_places=1,max_digits=4)
    YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
    )
    Presence_of_Ascites =models.CharField(choices=YES_NO_choise,max_length=20,null=True,blank=True)
    Presence_of_Focal_Lesions = models.CharField(choices=YES_NO_choise,max_length=20,null=True,blank=True)
    Performance_Status_In_Presence_of_Focal_Lesions =models.CharField(max_length=200,null=True,blank=True)
    Fib4 = models.DecimalField(null=True,decimal_places=1,max_digits=4,blank=True)
    Child_Score_choise = (
        ('A5','A5'),
        ('A6','A6'),
        ('B7','B7'),
        ('B8','B8'),
        ('B9','B9'),
        ('C','C'),

    )
    Child_Score =models.CharField(choices=Child_Score_choise,max_length=12,null=True,blank=True)
    HCC_Confirmed_by_Triphasic_CT_MRI= models.CharField(choices=YES_NO_choise,max_length=20,null=True,blank=True)
    Method_of_HCC_Confirmation_choise = (
        ('Triphasic CT','Triphasic CT'),
        ('MRI','MRI'),
    )
    Method_of_HCC_Confirmation = models.CharField(max_length=20,choices=Method_of_HCC_Confirmation_choise,null=True,blank=True)
    Number_of_focal_lesions = models.IntegerField(null=True,blank=True)
    Site_Segment = models.IntegerField(null=True,blank=True)
    Size_In_case_of_Multiple_lesions_mention_the_largest = models.CharField(max_length=50,null=True,blank=True)
    Attach_CT_Report_and_CT_Images_If_possible = models.FileField(upload_to='report',null=True,blank=True)
    Period_between_HCV_Cure_HCC_in_Months = models.IntegerField(null=True,blank=True)
    Hemoglobin = models.IntegerField(null=True,blank=True)
    Platelet_count = models.IntegerField(null=True,blank=True)
    WBCx103mm3 = models.IntegerField(null=True,blank=True)
    INR = models.DecimalField(null=True,decimal_places=1,max_digits=3,blank=True)
    Total_BILIRUBIN_mgdL = models.IntegerField(null=True,blank=True)
    Albumin_gdL= models.DecimalField(null=True,decimal_places=2,max_digits=4,blank=True)
    AST_IUL =models.DecimalField(null=True,decimal_places=2,max_digits=4)
    ALT_IUL =models.DecimalField(null=True,decimal_places=2,max_digits=4)
    Creatinine=models.DecimalField(null=True,decimal_places=2,max_digits=4,blank=True)
    date_of_the_last_dose = models.DateField(null=True,blank=True)
    Fup_befor = models.CharField(choices=YES_NO_choise,null=True ,max_length=20,blank=True)
    create_on = models.DateField(auto_now_add=True)



    def __str__(self):
        return  str(self.inrollment_id)
