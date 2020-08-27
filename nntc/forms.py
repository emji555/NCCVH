from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


from .models import Patient , W0, W4, W8 , W12 ,W16 , W20 ,W24 , W28 ,W36 , phy





class PatientForm(forms.ModelForm):
    Patient_Name = forms.CharField(max_length=100,label='Patient Name ',required=True,widget=forms.TextInput( attrs={ 'class':"form-control"}))
    Age =forms.IntegerField(max_value=100,min_value=18 ,required=True,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    National_ID =forms.CharField(max_length=14,label='National ID',required=True,validators=[RegexValidator('(2|3)[0-9][1-9][0-1][1-9][0-3][1-9](01|02|03|04|11|12|13|14|15|16|17|18|19|21|22|23|24|25|26|27|28|29|31|32|33|34|35|88)\d\d\d\d\d',message="please enter avalid national ID")],widget=forms.NumberInput( attrs={ 'class':"form-control"}))

    date = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control"}))
    Mobile_1 = forms.CharField(required=True,validators=[RegexValidator('(01)[0-9]{9}',message='please enter Avild phone number')],widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Mobile_2 =forms.CharField(required=False,validators=[RegexValidator('(01)[0-9]{9}',message='please enter Avild phone number')],widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Weight_Kgm =forms.DecimalField(required=False,max_value=442 ,min_value=30,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Height_m = forms.DecimalField(required=False,max_value=2.72,min_value=.21,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALT_IU_L = forms.DecimalField(min_value=10 ,max_value=2000,label='ALT(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALT_ULN = forms.DecimalField(min_value=10 ,max_value=2000,label='ALT(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AST_IU_L = forms.DecimalField(min_value=1 ,max_value=2000,label='AST(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AST_ULN = forms.DecimalField(min_value=1 ,max_value=2000,label='AST(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALP_IU_L=forms.DecimalField(min_value=10  ,max_value=500, required=False,label=' ALP(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALP_ULN=forms.DecimalField(min_value=10  ,max_value=500, required=False,label='ALP(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AFP_IU_L = forms.DecimalField(min_value=1  ,max_value=20000, required=False,label='AFP(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Total_BILIRUBIN_mg_d=forms.DecimalField(min_value=0.3  ,max_value=10,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Indirect_Bilirubin_mg_dL =forms.DecimalField(min_value=0.3   ,max_value=10, required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    GGT_IU_L =forms.DecimalField(min_value=10 ,max_value=500,label='GGT(IUL) ',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    GGT_ULN =forms.DecimalField(min_value=10 ,max_value=500,label='GGT(ULN)',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Plateletsx10_3 =forms.IntegerField(min_value=50  ,max_value=800,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    WBCx10_3_mm_3 =forms.DecimalField(min_value=0.2  ,max_value=30,required=True,label='WBCX10 3mm',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ANCx10_3_mm_3 =forms.DecimalField(min_value=0.2  ,max_value=20,label='ANCx10mm3',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Albumin_g_dL =forms.DecimalField(min_value=1  ,max_value=6,label='Abbumin (GDL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Hb_G_L =forms.IntegerField(min_value=6  ,max_value=18,label='HB(GL)',required=True,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    INR =forms.DecimalField(min_value=.1  ,max_value=4,label='INR',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Creatine_mg_dL=forms.DecimalField(min_value=.2  ,max_value=20,label='Creatine mg (dL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Glucose_mg_dL=forms.DecimalField(min_value=50  ,max_value=700,required=False,label='Glucose mg (dL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Triglyceride_mg_dl =forms.IntegerField(min_value=50  ,max_value=2000,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    LDL_mg_dl =forms.IntegerField(min_value=40  ,max_value=500,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    HDL_mg_dl =forms.IntegerField(min_value=20  ,max_value=100,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    TSH =forms.IntegerField(min_value=20  ,max_value=100,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    PC=forms.IntegerField(min_value=35  ,max_value=120,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    HBV_DNA_Quant=forms.IntegerField(min_value=1  ,max_value=20000000 ,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))



    class Meta:
        model = Patient
        fields = (
                'Patient_Name','date','Center_ID','National_ID','gender','Age',
                'Portal_number','Cohort','PCR_Date','PhysicianName','year_of_HCV_positivity',
                'Circumstances_of_referral','address','District_Town','Home_tel','Mobile_1','Mobile_2',
                'Treatment_Status','Which_kind_of_Treatment','Which_kind_of_Treatment_2','Other_Kind_of_Treatment',
                'Previous_treatment_last_injection_date','Weight_Kgm','Height_m','BMI','Tobacco_Consumption','Alcohol_intake',
                'Former_Or_Ongoing_IV_Drug_User','Blood_Pressure_Systolic_mmHg','Blood_Pressure_Diastolic_mmHg',
                'hypertensions','Diabetes','DM_Treatment','Known_to_be_cirrhotic','Hepatic_Encephalopathy',
                'Spicial_Situation','Spicial_Situation_Other','HCC','If_proVen_HCC','if_Treated_Specify_HCC',
                'Current_intake_of_other_medication','Drug_Name_2','Start_Date_of_Medication_2','Duration_Month_2','Drug_Name_3',
                'Start_Date_of_Medication_3','Duration_Month_3','Drug_Name_4','Start_Date_of_Medication_4',
                'Drug_Name_1','Start_Date_of_Medication_1','Duration_Month_1','Duration_Month_4',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Pregnancy_Test','ALT_IU_L','ALT_ULN','ALT_Result',
                'AST_IU_L','AST_ULN','ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN','Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL',
                'GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3','ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L','INR',
                'Creatine_mg_dL','Glucose_mg_dL','Triglyceride_mg_dl','LDL_mg_dl','HDL_mg_dl','TSH','PC',
                'HbA1c','ANA','titre','blood_Sample_Storage','Specify_The_ID_Sample','HBs_Ag',
                'HBV_DBA','HBV_DNA_Quant','ECG','Spicify_ECG','HIV','limit_of_detetion_IU_ml','Echo','Spicify_Echo',
                'Foundus_Exam','Foundus_exam_specify','Date_Ultrasound','Liver','PV','PV_Dimeter_mm','Other_ultrasound',
                'Ascites','Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant',
                'Other_Comment_Ultrasound','Fibrosis_Assessment','Liver_Biopsy_Date','Activity_Grade_A',
                'Fibrosis_Stage_F','Steatosis','Fibroscan_date','Fibroscan','stiffness','Previous_Treatment_for_schistosomiasis',
                'Serology','titre_Sch','Fib4_Calculation','Chid_score_Calculation','E_CrCl_Calculation',
                'Varices','Upper_Endoscopy','Others_Endoscopy','Note','Contract_Type','Duration',
                'Final_Decision')

        widgets ={



              'Center_ID':forms.TextInput(attrs={ 'class':"form-control",'value':'','id':'emji','type':'hidden'}),
              #'Center_ID':forms.Select(attrs={ 'class':"form-control"}),
              'National_ID':forms.NumberInput(attrs={ 'class':"form-control" }),
               'gender':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Age':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Portal_number':forms.TextInput(attrs={ 'class':"form-control"}),
              'Cohort':forms.TextInput(attrs={ 'class':"form-control"}),
              'PCR_Date':forms.DateInput(attrs={ 'class':"form-control"}),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control",'required':"True"}),
              'year_of_HCV_positivity':forms.DateInput(attrs={ 'class':"form-control"}),
              'Circumstances_of_referral':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'address':forms.TextInput(attrs={ 'class':"form-control"}),

              'District_Town':forms.TextInput(attrs={ 'class':"form-control"}),
              'Home_tel':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Mobile_1':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Mobile_2':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Treatment_Status':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Which_kind_of_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'Which_kind_of_Treatment_2':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Kind_of_Treatment':forms.TextInput(attrs={ 'class':"form-control"}),
              'Previous_treatment_last_injection_date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Height_m':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BMI':forms.TextInput(attrs={ 'class':"form-control"}),
              'Tobacco_Consumption':forms.Select(attrs={ 'class':"form-control"}),
              'Alcohol_intake':forms.Select(attrs={ 'class':"form-control"}),
              'Former_Or_Ongoing_IV_Drug_User':forms.Select(attrs={ 'class':"form-control"}),
              'Blood_Pressure_Systolic_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Blood_Pressure_Diastolic_mmHg':forms.TextInput(attrs={ 'class':"form-control"}),
              'hypertensions':forms.Select(attrs={ 'class':"form-control"}),
              'Diabetes':forms.Select(attrs={ 'class':"form-control"}),
              'DM_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'Known_to_be_cirrhotic':forms.Select(attrs={ 'class':"form-control"}),
              'Hepatic_Encephalopathy':forms.Select(attrs={ 'class':"form-control"}),
              'Spicial_Situation':forms.Select(attrs={ 'class':"form-control"}),

              'Spicial_Situation_Other':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCC':forms.Select(attrs={ 'class':"form-control"}),
              'If_proVen_HCC':forms.Select(attrs={ 'class':"form-control"}),
              'if_Treated_Specify_HCC':forms.TextInput(attrs={ 'class':"form-control"}),
              'Current_intake_of_other_medication':forms.Select(attrs={ 'class':"form-control"}),
              'Drug_Name_1':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_1':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_1':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Drug_Name_2':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_2':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_2':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Drug_Name_3':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_3':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Drug_Name_4':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_4':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_4':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Pregnancy_Test':forms.Select(attrs={ 'class':"form-control" }),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control" ,'id':'ALTIU','required':"True"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control",'id':'ALTIN','required':"True"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control",'value':'','id':'ALTre'}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Triglyceride_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'LDL_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HDL_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANA':forms.Select(attrs={ 'class':"form-control"}),
              'titre':forms.TextInput(attrs={ 'class':"form-control"}),
              'blood_Sample_Storage':forms.Select(attrs={ 'class':"form-control"}),
              'Specify_The_ID_Sample':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HBs_Ag':forms.Select(attrs={ 'class':"form-control"}),
              'HBV_DBA':forms.Select(attrs={ 'class':"form-control"}),
              'HBV_DNA_Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ECG':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_ECG':forms.TextInput(attrs={ 'class':"form-control"}),
              'HIV':forms.Select(attrs={ 'class':"form-control"}),
              'limit_of_detetion_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Echo':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Echo':forms.TextInput(attrs={ 'class':"form-control"}),
              'Foundus_Exam':forms.Select(attrs={ 'class':"form-control"}),
              'Foundus_exam_specify':forms.TextInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"}),
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Fibrosis_Assessment':forms.Select(attrs={ 'class':"form-control"}),
              'Liver_Biopsy_Date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Activity_Grade_A':forms.Select(attrs={ 'class':"form-control"}),
              'Fibrosis_Stage_F':forms.Select(attrs={ 'class':"form-control"}),
              'Steatosis':forms.Select(attrs={ 'class':"form-control"}),
              'Fibroscan_date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Fibroscan':forms.Select(attrs={ 'class':"form-control"}),
              'stiffness':forms.TextInput(attrs={ 'class':"form-control"}),
              'Previous_Treatment_for_schistosomiasis':forms.Select(attrs={ 'class':"form-control"}),
              'Serology':forms.Select(attrs={ 'class':"form-control"}),
              'titre_Sch':forms.TextInput(attrs={ 'class':"form-control"}),
              'Fib4_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Chid_score_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'E_CrCl_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Varices':forms.Select(attrs={ 'class':"form-control"}),
              'Upper_Endoscopy':forms.Select(attrs={ 'class':"form-control"}),
              'Others_Endoscopy':forms.TextInput(attrs={ 'class':"form-control"}),
              'Note':forms.TextInput(attrs={ 'class':"form-control"}),
              'Contract_Type':forms.Select(attrs={ 'class':"form-control"}),
               'Duration':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Final_Decision':forms.Select(attrs={ 'class':"form-control",'required':"True"}),

                }


class EditPatientForm(forms.ModelForm):
    Patient_Name = forms.CharField(max_length=100,label='Patient Name ',required=True,widget=forms.TextInput( attrs={ 'class':"form-control"}))
    Age =forms.IntegerField(max_value=100,min_value=18 ,required=True,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    #National_ID =forms.CharField(max_length=14,label='National ID',required=True,validators=[RegexValidator('(2|3)[0-9][1-9][0-1][1-9][0-3][1-9](01|02|03|04|11|12|13|14|15|16|17|18|19|21|22|23|24|25|26|27|28|29|31|32|33|34|35|88)\d\d\d\d\d',message="please enter avalid national ID")],widget=forms.NumberInput( attrs={ 'class':"form-control"}))

    date = forms.DateField(widget=forms.DateInput(attrs={'class':"form-control"}))
    Mobile_1 = forms.CharField(required=True,validators=[RegexValidator('(01)[0-9]{9}',message='please enter Avild phone number')],widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Mobile_2 =forms.CharField(required=False,validators=[RegexValidator('(01)[0-9]{9}',message='please enter Avild phone number')],widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Weight_Kgm =forms.DecimalField(required=False,max_value=442 ,min_value=30,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Height_m = forms.DecimalField(required=False,max_value=2.72,min_value=.21,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALT_IU_L = forms.DecimalField(min_value=10 ,max_value=2000,label='ALT(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALT_ULN = forms.DecimalField(min_value=10 ,max_value=2000,label='ALT(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AST_IU_L = forms.DecimalField(min_value=1 ,max_value=2000,label='AST(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AST_ULN = forms.DecimalField(min_value=1 ,max_value=2000,label='AST(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALP_IU_L=forms.DecimalField(min_value=10  ,max_value=500, required=False,label=' ALP(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ALP_ULN=forms.DecimalField(min_value=10  ,max_value=500, required=False,label='ALP(ULN)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    AFP_IU_L = forms.DecimalField(min_value=1  ,max_value=20000, required=False,label='AFP(IUL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Total_BILIRUBIN_mg_d=forms.DecimalField(min_value=0.3  ,max_value=10,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Indirect_Bilirubin_mg_dL =forms.DecimalField(min_value=0.3   ,max_value=10, required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    GGT_IU_L =forms.DecimalField(min_value=10 ,max_value=500,label='GGT(IUL) ',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    GGT_ULN =forms.DecimalField(min_value=10 ,max_value=500,label='GGT(ULN)',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Plateletsx10_3 =forms.IntegerField(min_value=50  ,max_value=800,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    WBCx10_3_mm_3 =forms.DecimalField(min_value=0.2  ,max_value=30,required=True,label='WBCX10 3mm',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    ANCx10_3_mm_3 =forms.DecimalField(min_value=0.2  ,max_value=20,label='ANCx10mm3',required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Albumin_g_dL =forms.DecimalField(min_value=1  ,max_value=6,label='Abbumin (GDL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Hb_G_L =forms.IntegerField(min_value=6  ,max_value=18,label='HB(GL)',required=True,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    INR =forms.DecimalField(min_value=.1  ,max_value=4,label='INR',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Creatine_mg_dL=forms.DecimalField(min_value=.2  ,max_value=20,label='Creatine mg (dL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Glucose_mg_dL=forms.DecimalField(min_value=50  ,max_value=700,required=False,label='Glucose mg (dL)',widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    Triglyceride_mg_dl =forms.IntegerField(min_value=50  ,max_value=2000,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    LDL_mg_dl =forms.IntegerField(min_value=40  ,max_value=500,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    HDL_mg_dl =forms.IntegerField(min_value=20  ,max_value=100,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    TSH =forms.IntegerField(min_value=20  ,max_value=100,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    PC=forms.IntegerField(min_value=35  ,max_value=120,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))
    HBV_DNA_Quant=forms.IntegerField(min_value=1  ,max_value=20000000 ,required=False,widget=forms.NumberInput( attrs={ 'class':"form-control"}))

    class Meta:

        model = Patient
        fields = (
                'Patient_Name','date','gender','Age',
                'Portal_number','Cohort','PCR_Date','PhysicianName','year_of_HCV_positivity',
                'Circumstances_of_referral','address','District_Town','Home_tel','Mobile_1','Mobile_2',
                'Treatment_Status','Which_kind_of_Treatment','Which_kind_of_Treatment_2','Other_Kind_of_Treatment',
                'Previous_treatment_last_injection_date','Weight_Kgm','Height_m','BMI','Tobacco_Consumption','Alcohol_intake',
                'Former_Or_Ongoing_IV_Drug_User','Blood_Pressure_Systolic_mmHg','Blood_Pressure_Diastolic_mmHg',
                'hypertensions','Diabetes','DM_Treatment','Known_to_be_cirrhotic','Hepatic_Encephalopathy',
                'Spicial_Situation','Spicial_Situation_Other','HCC','If_proVen_HCC','if_Treated_Specify_HCC',
                'Current_intake_of_other_medication','Drug_Name_2','Start_Date_of_Medication_2','Duration_Month_2','Drug_Name_3',
                'Start_Date_of_Medication_3','Duration_Month_3','Drug_Name_4','Start_Date_of_Medication_4',
                'Drug_Name_1','Start_Date_of_Medication_1','Duration_Month_1','Duration_Month_4',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Pregnancy_Test','ALT_IU_L','ALT_ULN','ALT_Result',
                'AST_IU_L','AST_ULN','AST_Result','ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN','Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL',
                'GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3','ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L','INR',
                'Creatine_mg_dL','Glucose_mg_dL','Triglyceride_mg_dl','LDL_mg_dl','HDL_mg_dl','TSH','PC',
                'HbA1c','ANA','titre','blood_Sample_Storage','Specify_The_ID_Sample','HBs_Ag',
                'HBV_DBA','HBV_DNA_Quant','ECG','Spicify_ECG','HIV','limit_of_detetion_IU_ml','Echo','Spicify_Echo',
                'Foundus_Exam','Foundus_exam_specify','Date_Ultrasound','Liver','PV','PV_Dimeter_mm','Other_ultrasound',
                'Ascites','Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant',
                'Other_Comment_Ultrasound','Fibrosis_Assessment','Liver_Biopsy_Date','Activity_Grade_A',
                'Fibrosis_Stage_F','Steatosis','Fibroscan_date','Fibroscan','stiffness','Previous_Treatment_for_schistosomiasis',
                'Serology','titre_Sch','Fib4_Calculation','Chid_score_Calculation','E_CrCl_Calculation',
                'Varices','Upper_Endoscopy','Others_Endoscopy','Note','Contract_Type','Duration',
                'Final_Decision')

        widgets ={


             # 'Center_ID':forms.TextInput(attrs={ 'class':"form-control",'value':'','id':'emji','type':'hidden'}),
              #'Center_ID':forms.Select(attrs={ 'class':"form-control"}),
              #'National_ID':forms.NumberInput(attrs={ 'class':"form-control" }),
               'gender':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Age':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Portal_number':forms.TextInput(attrs={ 'class':"form-control"}),
              'Cohort':forms.TextInput(attrs={ 'class':"form-control"}),
              'PCR_Date':forms.DateInput(attrs={ 'class':"form-control"}),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control",'required':"True"}),
              'year_of_HCV_positivity':forms.DateInput(attrs={ 'class':"form-control"}),
              'Circumstances_of_referral':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'address':forms.TextInput(attrs={ 'class':"form-control"}),

              'District_Town':forms.TextInput(attrs={ 'class':"form-control"}),
              'Home_tel':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Mobile_1':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Mobile_2':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'Treatment_Status':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Which_kind_of_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'Which_kind_of_Treatment_2':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Kind_of_Treatment':forms.TextInput(attrs={ 'class':"form-control"}),
              'Previous_treatment_last_injection_date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Height_m':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BMI':forms.TextInput(attrs={ 'class':"form-control"}),
              'Tobacco_Consumption':forms.Select(attrs={ 'class':"form-control"}),
              'Alcohol_intake':forms.Select(attrs={ 'class':"form-control"}),
              'Former_Or_Ongoing_IV_Drug_User':forms.Select(attrs={ 'class':"form-control"}),
              'Blood_Pressure_Systolic_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Blood_Pressure_Diastolic_mmHg':forms.TextInput(attrs={ 'class':"form-control"}),
              'hypertensions':forms.Select(attrs={ 'class':"form-control"}),
              'Diabetes':forms.Select(attrs={ 'class':"form-control"}),
              'DM_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'Known_to_be_cirrhotic':forms.Select(attrs={ 'class':"form-control"}),
              'Hepatic_Encephalopathy':forms.Select(attrs={ 'class':"form-control"}),
              'Spicial_Situation':forms.Select(attrs={ 'class':"form-control"}),

              'Spicial_Situation_Other':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCC':forms.Select(attrs={ 'class':"form-control"}),
              'If_proVen_HCC':forms.Select(attrs={ 'class':"form-control"}),
              'if_Treated_Specify_HCC':forms.TextInput(attrs={ 'class':"form-control"}),
              'Current_intake_of_other_medication':forms.Select(attrs={ 'class':"form-control"}),
              'Drug_Name_1':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_1':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_1':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Drug_Name_2':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_2':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_2':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Drug_Name_3':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_3':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Drug_Name_4':forms.TextInput(attrs={ 'class':"form-control"}),
              'Start_Date_of_Medication_4':forms.DateInput(attrs={ 'class':"form-control"}),
              'Duration_Month_4':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Pregnancy_Test':forms.Select(attrs={ 'class':"form-control" }),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control" ,'id':'ALTIU','required':"True"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control",'id':'ALTIN','required':"True"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control",'required':"True"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Triglyceride_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'LDL_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HDL_mg_dl':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANA':forms.Select(attrs={ 'class':"form-control"}),
              'titre':forms.TextInput(attrs={ 'class':"form-control"}),
              'blood_Sample_Storage':forms.Select(attrs={ 'class':"form-control"}),
              'Specify_The_ID_Sample':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HBs_Ag':forms.Select(attrs={ 'class':"form-control"}),
              'HBV_DBA':forms.Select(attrs={ 'class':"form-control"}),
              'HBV_DNA_Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ECG':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_ECG':forms.TextInput(attrs={ 'class':"form-control"}),
              'HIV':forms.Select(attrs={ 'class':"form-control"}),
              'limit_of_detetion_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Echo':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Echo':forms.TextInput(attrs={ 'class':"form-control"}),
              'Foundus_Exam':forms.Select(attrs={ 'class':"form-control"}),
              'Foundus_exam_specify':forms.TextInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"}),
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Fibrosis_Assessment':forms.Select(attrs={ 'class':"form-control"}),
              'Liver_Biopsy_Date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Activity_Grade_A':forms.Select(attrs={ 'class':"form-control"}),
              'Fibrosis_Stage_F':forms.Select(attrs={ 'class':"form-control"}),
              'Steatosis':forms.Select(attrs={ 'class':"form-control"}),
              'Fibroscan_date':forms.DateInput(attrs={ 'class':"form-control"}),
              'Fibroscan':forms.Select(attrs={ 'class':"form-control"}),
              'stiffness':forms.TextInput(attrs={ 'class':"form-control"}),
              'Previous_Treatment_for_schistosomiasis':forms.Select(attrs={ 'class':"form-control"}),
              'Serology':forms.Select(attrs={ 'class':"form-control"}),
              'titre_Sch':forms.TextInput(attrs={ 'class':"form-control"}),
              'Fib4_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Chid_score_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'E_CrCl_Calculation':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Varices':forms.Select(attrs={ 'class':"form-control"}),
              'Upper_Endoscopy':forms.Select(attrs={ 'class':"form-control"}),
              'Others_Endoscopy':forms.TextInput(attrs={ 'class':"form-control"}),
              'Note':forms.TextInput(attrs={ 'class':"form-control"}),
              'Contract_Type':forms.Select(attrs={ 'class':"form-control"}),
               'Duration':forms.Select(attrs={ 'class':"form-control",'required':"True"}),
              'Final_Decision':forms.Select(attrs={ 'class':"form-control",'required':"True"}),


                }

################################################### W0 Form ################################################



class W0Form(forms.ModelForm):
    class Meta:
        model = W0
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound','Ribavirine_dose','INF_Dose',
                'SOF_Dose','SIM_Dose','LED','DAC','PAR_OMB','additional',
                'Other','presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects',
                'Decision_To','New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment'
                )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ribavirine_dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'SOF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),

              'SIM_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'LED':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PAR_OMB':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional':forms.TextInput(attrs={ 'class':"form-control"}),
              'Other':forms.TextInput(attrs={ 'class':"form-control"}),
              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),



                }

class W0FormUpdate(forms.ModelForm):
    class Meta:
        model = W0
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound','Ribavirine_dose','INF_Dose',
                'SOF_Dose','SIM_Dose','LED','DAC','PAR_OMB','additional',
                'Other','presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects',
                'Decision_To','New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment'
                )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ribavirine_dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'SOF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),

              'SIM_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'LED':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PAR_OMB':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional':forms.TextInput(attrs={ 'class':"form-control"}),
              'Other':forms.TextInput(attrs={ 'class':"form-control"}),
              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),



                }





###############################################  W4 ########################################

class W4Form(forms.ModelForm):
    class Meta:
        model = W4
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment','HCV_RNA_W4'
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W4':forms.Select(attrs={ 'class':"form-control"}),



                }

class W4FormUpdate(forms.ModelForm):
    class Meta:
        model = W4
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment','HCV_RNA_W4'
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W4':forms.Select(attrs={ 'class':"form-control"}),



                }


#########################################W 8 add


class W8Form(forms.ModelForm):
    class Meta:
        model = W8
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }
class W8FormUpdate(forms.ModelForm):
    class Meta:
        model = W8
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }


    #######################################W12 create form  #################################

class W12Form(forms.ModelForm):
        class Meta:
            model = W12
            fields = (



                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                  'HCV_RNA_W12','HIV_PCR_W12', 'HIV_PCR_Value_12')

            widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W12':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W12':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_12':forms.NumberInput(attrs={ 'class':"form-control"}),




                }

class W12FormUpdate(forms.ModelForm):
        class Meta:
            model = W12
            fields = (



                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                  'HCV_RNA_W12','HIV_PCR_W12', 'HIV_PCR_Value_12')

            widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W12':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W12':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_12':forms.NumberInput(attrs={ 'class':"form-control"}),




                }

########################################W16 create form #####################3


class W16Form(forms.ModelForm):
    class Meta:
        model = W16
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }

class W16FormUpdate(forms.ModelForm):
    class Meta:
        model = W16
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }

######################################## W20 create form ########################

class W20Form(forms.ModelForm):
    class Meta:
        model = W20
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }

class W20FormUpdate(forms.ModelForm):
    class Meta:
        model = W20
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }


###########################################w24 create form ###############################


class W24Form(forms.ModelForm):
    class Meta:
        model = W24
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                   'HCV_RNA_W24','HIV_PCR_W24' ,'HIV_PCR_Value_24','CD4_count_W24')

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W24':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W24':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_24':forms.NumberInput(attrs={ 'class':"form-control"}),
              'CD4_count_W24':forms.NumberInput(attrs={ 'class':"form-control"}),




                }

class W24FormUpdate(forms.ModelForm):
    class Meta:
        model = W24
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                   'HCV_RNA_W24','HIV_PCR_W24' ,'HIV_PCR_Value_24','CD4_count_W24')

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W24':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W24':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_24':forms.NumberInput(attrs={ 'class':"form-control"}),
              'CD4_count_W24':forms.NumberInput(attrs={ 'class':"form-control"}),




                }




#################################   W 28 add Week ##############################

class W28Form(forms.ModelForm):
    class Meta:
        model = W28
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }

class W28FormUpdate(forms.ModelForm):
    class Meta:
        model = W28
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                    )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),




                }
#######################################add New Week 36
class W36Form(forms.ModelForm):
    class Meta:
        model = W36
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                  'HCV_RNA_W36','HIV_PCR_W36','HIV_PCR_Value_36','CD4_count_W36'  )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W36':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W36':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_36':forms.NumberInput(attrs={ 'class':"form-control"}),
              'CD4_count_W36':forms.NumberInput(attrs={ 'class':"form-control"}),




                }


class W36FormUpdate(forms.ModelForm):
    class Meta:
        model = W36
        fields = (
                'FollowUp_date','PhysicianName','date',
                'HCV_RNA','Quant','Limit_OF_Det_IU_ml','Weight_Kgm','BP_mmHg',
                'ALT_IU_L','ALT_ULN','ALT_Result','AST_IU_L','AST_ULN','AST_Result',
                'ALP_IU_L','ALP_ULN','AFP_IU_L','AFP_ULN',
                'Total_BILIRUBIN_mg_d','Indirect_Bilirubin_mg_dL','GGT_IU_L','GGT_ULN','Plateletsx10_3','WBCx10_3_mm_3',
                'ANCx10_3_mm_3','Albumin_g_dL','Hb_G_L',
                'INR','Creatine_mg_dL','Glucose_mg_dL','TSH','PC',
                'HbA1c','Date_Ultrasound','Liver','PV','PV_Dimeter_mm',
                'Other_ultrasound','Ascites', 'Ascites_IF_YES','Presence_Of_focal_Lesions','If_Presence_Of_focal_Lesions_yes_number',
                'Diameter_Of_Largest_cm','sonographic_Appearance_Malignant','Other_Comment_Ultrasound',

                'presence_of_Side_Effects','If_Presence_Of_side_effect_yes','spicify_side_Effects','Decision_To',
                'New_Ribavirin_Dose','New_INF_Dose','additional_sideEffect','Stop_Treatment_Options','Spicify_Stop_Treatment',
                  'HCV_RNA_W36','HIV_PCR_W36','HIV_PCR_Value_36','CD4_count_W36'  )

        widgets ={


               'date':forms.DateInput(attrs={ 'class':"form-control" }),

              'FollowUp_date':forms.DateInput(attrs={ 'class':"form-control" }),
              'PhysicianName':forms.TextInput(attrs={ 'class':"form-control"}),
              'HCV_RNA':forms.Select(attrs={ 'class':"form-control"}),
              'Quant':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Limit_OF_Det_IU_ml':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Weight_Kgm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'BP_mmHg':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALT_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AST_Result':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ALP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'AFP_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Total_BILIRUBIN_mg_d':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Indirect_Bilirubin_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_IU_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'GGT_ULN':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Plateletsx10_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'WBCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'ANCx10_3_mm_3':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Albumin_g_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Hb_G_L':forms.NumberInput(attrs={ 'class':"form-control"}),
              'INR':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Creatine_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),

              'Glucose_mg_dL':forms.NumberInput(attrs={ 'class':"form-control"}),
              'TSH':forms.NumberInput(attrs={ 'class':"form-control"}),
              'PC':forms.NumberInput(attrs={ 'class':"form-control"}),
              'HbA1c':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Date_Ultrasound':forms.DateInput(attrs={ 'class':"form-control"}),
              'Liver':forms.Select(attrs={ 'class':"form-control"}),
              'PV':forms.Select(attrs={ 'class':"form-control"}),
              'PV_Dimeter_mm':forms.NumberInput(attrs={ 'class':"form-control"})  ,
              'Other_ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),
              'Ascites':forms.Select(attrs={ 'class':"form-control"}),
              'Ascites_IF_YES':forms.Select(attrs={ 'class':"form-control"})  ,
              'Presence_Of_focal_Lesions':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_focal_Lesions_yes_number':forms.NumberInput(attrs={ 'class':"form-control"}),
              'Diameter_Of_Largest_cm':forms.NumberInput(attrs={ 'class':"form-control"}),
              'sonographic_Appearance_Malignant':forms.Select(attrs={ 'class':"form-control"}),
              'Other_Comment_Ultrasound':forms.TextInput(attrs={ 'class':"form-control"}),


              'presence_of_Side_Effects':forms.Select(attrs={ 'class':"form-control"}),
              'If_Presence_Of_side_effect_yes':forms.Select(attrs={ 'class':"form-control"}),
              'spicify_side_Effects':forms.TextInput(attrs={ 'class':"form-control"}),
              'Decision_To':forms.Select(attrs={ 'class':"form-control"}),
              'New_Ribavirin_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'New_INF_Dose':forms.NumberInput(attrs={ 'class':"form-control"}),
              'additional_sideEffect':forms.TextInput(attrs={ 'class':"form-control"}),



              'Stop_Treatment_Options':forms.Select(attrs={ 'class':"form-control"}),
              'Spicify_Stop_Treatment':forms.Select(attrs={ 'class':"form-control"}),
              'HCV_RNA_W36':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_W36':forms.Select(attrs={ 'class':"form-control"}),
              'HIV_PCR_Value_36':forms.NumberInput(attrs={ 'class':"form-control"}),
              'CD4_count_W36':forms.NumberInput(attrs={ 'class':"form-control"}),




                }
#################################Phytions#######################


class phyForm(forms.ModelForm):
    Phythion_Name = forms.CharField(max_length=100,label='Physion Name ',required=True,widget=forms.TextInput( attrs={ 'class':"form-control"}))




    class Meta:
        model = phy
        fields = (
                'Phythion_Name','Phythion_Center',)

        widgets ={



              'Phythion_Center':forms.TextInput(attrs={ 'class':"form-control",'value':'','id':'emji','type':'hidden'}),
              #'Center_ID':forms.Select(attrs={ 'class':"form-control"}),

                }


class EditPhyForm(forms.ModelForm):

    class Meta:

        model = phy
        fields = (
                'Phythion_Name',
               )

        widgets ={

              'Phythion_Name':forms.TimeInput(attrs={ 'class':"form-control"}),



                }
