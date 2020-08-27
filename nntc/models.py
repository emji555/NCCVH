from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date


# Create your models here.
class phy(models.Model):
     Phythion_Name = models.CharField(null=True,blank=True,max_length=20)
     Phythion_Center = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
     def __str__(self):
          return '%s -%s' % (self.Phythion_Center.username,self.Phythion_Name)
     def get_absolute_url(self):
          return reverse('home')

#########################################################################################################
class Profile(models.Model):
     user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
     numberofPatient =models.IntegerField(null=True)

     def __str__(self):
          return str(self.user)


class Patient(models.Model):
    Patient_Name = models.CharField(max_length=200, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    Center_ID=models.ForeignKey(User,on_delete=models.SET_NULL, null=True)


    National_ID = models.CharField(primary_key=True, max_length=14, null=False)
    Gender_choices=(
        ('Male','Male'),
        ('Female','Female'),
    )
    gender=models.CharField(choices=Gender_choices, max_length=300,null=True,blank=True)
    Age = models.IntegerField(null=True)
    Portal_number = models.CharField(max_length=20, null=True,blank=True)
    Cohort = models.CharField(max_length=200,blank=True,null=True)
    PCR_Date = models.DateField(null=True,blank=True)
     #end of patient information
    PhysicianName=models.CharField(max_length=200, null=True,blank=True)
    year_of_HCV_positivity = models.DateField(null=True,blank=True)

    Circumstances_of_referral_choices = (
        ('تحويل قوافل', 'تحويل قوافل'),
        ('موقع الحجز', 'موقع الحجز'),
        ('موقع الحجز', 'موقع الحجز'),
        ('مستشفات', 'مستشفات'),
        ('مبادرة المسح', 'مبادرة المسح'),
        ('طلبة', 'طلبة'),
        ('سجون', 'سجون'),
        ('راغبى السفر', 'راغبى السفر'),
        ('مسح ميدانى', 'مسح ميدانى'),
        ('Routine Check-up', 'Routine Check-up'),
        ('Blood donation', 'Blood donation'),
        ('Mass campaign', 'Mass campaign'),
        ('Known risk factors', 'Known risk factors'),
        ('Unknown', 'Unknown'),

    )
    Circumstances_of_referral = models.CharField(
        choices=Circumstances_of_referral_choices, max_length=300,blank=True,null=True)

    #end of GEBERAL STATUS
    address = models.CharField(max_length=300, null=True,blank=True)
    District_Town = models.CharField(max_length=200, null=True,blank=True)
    Home_tel = models.CharField(max_length=200, null=True,blank=True)
    Mobile_1 = models.CharField(max_length=200, null=True,blank=True)
    Mobile_2 = models.CharField(max_length=200, null=True,blank=True)
  #end of indentification form

    Treatment_Status_choise = (
         ('Treatment Naive', 'Treatment Naive'),
         ('Treatment Experienced', 'Treatment Experienced'))

    Treatment_Status = models.CharField(
        choices=Treatment_Status_choise, null=True, max_length=200)
    Which_kind_of_Treatment_choise = (
         ('Other', 'Other'),
         ('Old Interferon Protocol', 'Old Interferon Protocol'),
         ('Roche', 'Roche'),
         ('SOF/RBV', 'SOF/RBV'),
         ('INF/SOF/RBV', 'INF/SOF/RBV'),
         ('SOF/DAC', 'SOF/DAC'),
         ('SOF/DAC/RBV', 'SOF/DAC/RBV'),
         ('SIM/SOF', 'SIM/SOF'),
         ('SOF/SIM/DAC/RBV', 'SOF/SIM/DAC/RBV'),
         ('SOF/SIM/DAC', 'SOF/SIM/DAC'),
         ('PAR/OMB', 'PAR/OMB'),
         ('PAR/OMB/RBV', 'PAR/OMB/RBV'),
         ('INF/RBV', 'INFRBV'),
         ('SOF/PAR/OMP', 'SOF/PAR/OMP'),
         ('PAR/OMB/RBV', 'PAR/OMB/RBV'),
         ('SOF/PAR/OMB/RBV', 'SOF/PAR/OMB/RBV'),
     )

    Which_kind_of_Treatment = models.CharField(
         choices=Which_kind_of_Treatment_choise, max_length=200,null=True,blank=True)
    Which_kind_of_Treatment_2 = models.CharField(
         choices=Which_kind_of_Treatment_choise, max_length=200,null=True,blank=True)
    Other_Kind_of_Treatment = models.CharField(max_length=200,null=True,blank=True)
    Previous_treatment_last_injection_date = models.DateField(null=True,blank=True)
      #end of Treatment status
    Weight_Kgm = models.IntegerField(null=True,blank=True)
    Height_m = models.FloatField(null=True, max_length=200,blank=True)
    BMI = models.FloatField(null=True, max_length=200,blank=True)
    YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )

    Tobacco_Consumption = models.CharField(
         choices=YES_NO_choise, null=True, max_length=200,blank=True)
    Alcohol_intake = models.CharField(
         choices=YES_NO_choise, null=True, max_length=200,blank=True)
    Former_Or_Ongoing_IV_Drug_User = models.CharField(
         choices=YES_NO_choise, max_length=200,blank=True,null=True)
    Blood_Pressure_Systolic_mmHg = models.IntegerField(null=True,blank=True)
    Blood_Pressure_Diastolic_mmHg = models.IntegerField(null=True,blank=True)
      #end of Clinical Information
    hypertensions = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
    Diabetes = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
    DM_Treatment_choise = (
         ('Only Diet', 'Only Diet'),
         ('Oral', 'Oral'),
         ('Insulin', 'Insulin'),
         ('Both', 'Both'),
     )
    DM_Treatment = models.CharField(
         choices=DM_Treatment_choise, max_length=200,null=True,blank=True)
    Known_to_be_cirrhotic = models.CharField(
         choices=YES_NO_choise, max_length=200,null=True,blank=True)
    Hepatic_Encephalopathy = models.CharField(
         choices=YES_NO_choise, max_length=200,null=True,blank=True)
    Spicial_Situation_choise = (
         ('On Dailysis', 'On Dailysis'),
         ('Post-Transplant', 'Post-Transplant'),
         ('Post-Chemotherapy', 'Post-Chemotherapy'),
         ('Autoimmune Disease', 'Autoimmune Disease'),
         ('Post-Transplant Kidney', 'Post-Transplant Kidney'),
         ('Post-Transplant Liver', 'Post-Transplant Liver'),
         ('Extrahepatic', 'Extrahepatic'),
         ('Others', 'Others'),

     )

    Spicial_Situation = models.CharField(
         choices=Spicial_Situation_choise, max_length=200,null=True,blank=True)
    Spicial_Situation_Other = models.CharField(max_length=200, null=True,blank=True)
    HCC = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
    If_proVen_HCC_choise = (
         ('Regional Therapy', 'Regional Therapy'),
         ('Treated', 'Treated'),
         ('Not Treated', 'Not Treated'),

     )
    If_proVen_HCC = models.CharField(
         choices=If_proVen_HCC_choise, null=True, max_length=200,blank=True)
    if_Treated_Specify_HCC = models.CharField(max_length=500,blank=True,null=True)
    Current_intake_of_other_medication = models.CharField(
         choices=YES_NO_choise, max_length=200,null=True,blank=True)
    Drug_Name_1 = models.CharField(max_length=300, null=True,blank=True)
    Start_Date_of_Medication_1 = models.DateField(null=True,blank=True)
    Duration_Month_1 = models.IntegerField(null=True,blank=True)
    Drug_Name_2 = models.CharField(max_length=300, null=True,blank=True)
    Start_Date_of_Medication_2 = models.DateField(null=True,blank=True)
    Duration_Month_2 = models.IntegerField(null=True,blank=True)
    Drug_Name_3 = models.CharField(max_length=300, null=True,blank=True)
    Start_Date_of_Medication_3 = models.DateField(null=True,blank=True)
    Duration_Month_3 = models.IntegerField(null=True,blank=True)
    Drug_Name_4 = models.CharField(max_length=300, null=True,blank=True)
    Start_Date_of_Medication_4 = models.DateField(null=True,blank=True)
    Duration_Month_4 = models.IntegerField(null=True,blank=True)
     # end of Chronic Disease

    P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )

    HCV_RNA = models.CharField(choices=P_N_Choise,  max_length=200,null=True,blank=True)
    Quant = models.IntegerField(null=True,blank=True)
    Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)

    Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )
    Pregnancy_Test = models.CharField(choices=Not_Done_Choise, max_length=200,null=True,blank=True)
    ALT_IU_L = models.FloatField(null=True, max_length=200)
    ALT_ULN = models.FloatField(null=True, max_length=200)
    ALT_Result = models.CharField(null=True, max_length=200,blank=True)
    AST_IU_L = models.FloatField(null=True, max_length=200)
    AST_ULN = models.FloatField(null=True, max_length=200)
    AST_Result = models.FloatField(null=True, max_length=200,blank=True)
    ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
    ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
    AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
    AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
    Total_BILIRUBIN_mg_d = models.FloatField(null=True)
    Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
    GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
    GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
    Plateletsx10_3 = models.IntegerField(null=True)
    WBCx10_3_mm_3 = models.FloatField(null=True)
    ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
    Albumin_g_dL = models.FloatField(null=True)
    Hb_G_L = models.IntegerField(null=True)
    INR = models.FloatField(null=True, max_length=200)
    Creatine_mg_dL = models.FloatField(null=True, max_length=200)
    Glucose_mg_dL = models.FloatField(null=True, max_length=200)
    Triglyceride_mg_dl = models.FloatField(null=True, max_length=200,blank=True)
    LDL_mg_dl = models.FloatField(null=True, max_length=200,blank=True)
    HDL_mg_dl = models.FloatField(null=True, max_length=200,blank=True)
    TSH = models.FloatField(null=True, max_length=200,blank=True)
    PC = models.FloatField(null=True, max_length=200,blank=True)
    HbA1c = models.FloatField(null=True, max_length=200,blank=True)
    ANA = models.CharField(choices=Not_Done_Choise, null=True, max_length=200,blank=True)
    titre = models.CharField(max_length=200,blank=True,null=True)
    blood_Sample_Storage = models.CharField(
         choices=YES_NO_choise, max_length=11 ,null=True,blank=True)
    Specify_The_ID_Sample = models.IntegerField(null=True,blank=True)
    #  end of Lab result
    HBs_Ag = models.CharField(choices=Not_Done_Choise, max_length=200,null=True,blank=True)
    HBV_DBA = models.CharField(choices=Not_Done_Choise, max_length=200,null=True,blank=True)
    HBV_DNA_Quant = models.IntegerField(null=True,default=0,blank=True)
    ECG_choise = (
         ('Normal', 'Normal'),
         ('Abnormal', 'Abnormal'),
         ('Not Done', 'Not Done'),
     )
    ECG = models.CharField(choices=ECG_choise, max_length=200,null=True,blank=True)
    Spicify_ECG = models.TextField(null=True,blank=True)
    HIV = models.CharField(choices=Not_Done_Choise, max_length=200,null=True,blank=True)
    limit_of_detetion_IU_ml = models.IntegerField(null=True,blank=True)
    Echo = models.CharField(choices=ECG_choise, max_length=200,null=True,blank=True)
    Spicify_Echo = models.TextField(null=True,blank=True)

    #End Chronic Heptitis B
    Foundus_Exam = models.CharField(choices=Not_Done_Choise, max_length=200,null=True,blank=True)
    Foundus_exam_specify = models.TextField(null=True,blank=True)
     # end of fundus exam
    Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
    Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
    Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
    PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
    PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
    PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
    Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
    Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
    Ascites_choices = (
         ('Mild-Moderate', 'Mild-Moderate'),
         ('Tense', 'Tense'),
         ('mild-moderate', 'mild-moderate'),
     )
    Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,null=True,blank=True)
    Presence_Of_focal_Lesions = models.CharField(
         choices=YES_NO_choise, max_length=200,null=True,blank=True)
    If_Presence_Of_focal_Lesions_yes_number = models.CharField(
         null=True, max_length=200,blank=True)
    Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

    sonographic_Appearance_Malignant_choices = (
         ('Yes', 'Yes'),
         ('No', 'No'),
         ('Suspicious', 'Suspicious'),
     )
    sonographic_Appearance_Malignant = models.CharField(
         choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
    Other_Comment_Ultrasound = models.TextField(null=True,blank=True)

     # end of Abdominal Ultrasound

    #end of fibrosis_Assessment

    Fibrosis_Assessment_Chosice = (
         ('Liver Biopsy (Metavir)', 'Liver Biopsy (Metavir)'),
         ('Fibroscan', 'Fibroscan'),
         ('Both', 'Both'),
         ('No Need', 'No Need'),

     )

    Fibrosis_Assessment = models.CharField(
         choices=Fibrosis_Assessment_Chosice, max_length=200,null=True,blank=True)
    Activity_Grade_A_choices = (
         ('A0', 'A0'),
         ('A1', 'A1'),
         ('A2', 'A2'),
         ('A3', 'A3'),
     )
    Liver_Biopsy_Date = models.DateField(null=True,blank=True)

    Activity_Grade_A = models.CharField(
         choices=Activity_Grade_A_choices, max_length=200,null=True,blank=True)
    Fibrosis_Stage_F_choices = (
         ('F0', 'F0'),
         ('F1', 'F1'),
         ('F2', 'F2'),
         ('F3', 'F3'),
         ('F4', 'F4'),
     )
    Fibrosis_Stage_F = models.CharField(
         choices=Fibrosis_Assessment_Chosice, max_length=200,null=True,blank=True)
    Steatosis_choise = (
         ('None', 'None'),
         ('Mild(1-32%)', 'Mild(1-32%)',),
         ('Moderate(33-66%)', 'Moderate(33-66%)'),
         ('Severe(>66%)', 'Severe(>66%)'),
     )
    Steatosis = models.CharField(choices=Steatosis_choise, max_length=200,null=True,blank=True)
    #end of liver Biopsy

    Fibroscan_date = models.DateField(null=True,blank=True)
    Fibroscan_choices = (
         ('F0', 'F0'),
         ('F0-1', 'F0-1'),
         ('F1', 'F1'),
         ('F1-2', 'F1-2'),
         ('F2', 'F2'),
         ('F2-3', 'F2-3'),
         ('F3', 'F3'),
         ('F3', 'F3'),
         ('F3-4', 'F3-4'),
         ('F4', 'F4'),

     )

    Fibroscan = models.CharField(choices=Fibroscan_choices, max_length=200,null=True,blank=True)
    stiffness = models.CharField(null=True, max_length=200,blank=True)

  #End of Fibrosis Assessment

    Previous_Treatment_for_schistosomiasis_choices = (
         ('Yes', 'Yes'),
         ('No', 'No'),
         ('Recent Treatment', 'Recent Treatment'),
         ('Past Treatment', 'Past Treatment'),

     )
    Previous_Treatment_for_schistosomiasis = models.CharField(
         choices=Previous_Treatment_for_schistosomiasis_choices, max_length=200,null=True,blank=True)
    Serology = models.CharField(choices=P_N_Choise, max_length=200,null=True,blank=True)
    titre_Sch = models.CharField(max_length=200, null=True,blank=True)
     # end of Schistosomiasis
    Fib4_Calculation = models.FloatField(null=True, max_length=200,blank=True)
    Chid_score_Calculation = models.FloatField(null=True, max_length=200,blank=True)
    E_CrCl_Calculation = models.FloatField(null=True, max_length=200,blank=True)
    Varices_choices = (
         ('Risky Varices', 'Risky Varices'),
         ('Not Risky', 'Not Risky'),
         ('Eradicated', 'Eradicated'),
     )
    Varices = models.CharField(choices=Varices_choices, max_length=200,null=True,blank=True)
    Upper_Endoscopy_choices = (
         ('Not pereformed', 'Not pereformed'),
         ('Free', 'Free'),
         ('Others', 'Others'),
         ('Varices', 'Varices'),
     )
    Upper_Endoscopy = models.CharField(
         choices=Upper_Endoscopy_choices, max_length=200,null=True,blank=True)
    Others_Endoscopy = models.TextField(null=True,blank=True)

    #  End OF Calculations
    Code_List_choise = (
         ('1) Psychiatric Disorders', '1) Psychiatric Disorders'),
         ('2) Cardiac Disease', '2) Cardiac Disease'),
         ('3) Thyroid Abnormalities', '3) Thyroid Abnormalities'),
         ('4) Post Transplant', '4) Post Transplant'),
         ('5) Autoimmune disease', '5) Autoimmune disease'),
         ('6) Proliferative Retinnopathy', '6) Proliferative Retinnopathy'),
         ('7) Esophageal Varices', '7) Esophageal Varices'),
         ('8) Anemia', '8) Anemia'),
         ('9) Thrombocytopenia', '9) Thrombocytopenia'),
         ('10) Leucopenia', '10) Leucopenia'),
         ('11) Neutropenia', '11) Neutropenia'),
         ('12) Extrahepatic', '12) Extrahepatic'),
         ('13) Others', '13) Others'),
         ('14) Age >60', '14) Age >60'),
         ('15) Decompensated cirrhosis', '15) Decompensated cirrhosis'),
         ('16) Severe Fundus Abnormalities', '16) Severe Fundus Abnormalities'),
         ('other','other')

     )
    Code_List= models.CharField(max_length=200,null=True,blank=True,choices=Code_List_choise,default='other')
    Note = models.TextField(blank = True,null=True)
    #Note = models.TextField(null=True)

    Contract_Type_choices = (
         ('Governmental Support', 'Governmental Support'),
         ('Health Insurance', 'Health Insurance'),
         ('Private', 'Private'),
         ('Cash', 'Cash'),
         ('Tahia MISR', 'Tahia MISR'),
         ('Beet EL-Zkah', 'Beet EL-Zkah'),
         ('مبادرة المسح', 'مبادرة المسح'),

     )

    Contract_Type = models.CharField(
         choices=Contract_Type_choices, max_length=200,null=True,blank=True)

    Duration_choices = (
         ('12 Week', '12 Week'),
         ('24 Week', '24 Week'),
         ('No Duration', 'No Duration')

     )
    Duration = models.CharField(choices=Duration_choices, max_length=200,null=True,blank=True)

    Final_Decision_Choices = (
         ('SOF/RBV', 'SOF/RBV'),
         ('INF/SOF/RBV', 'INF/SOF/RBV'),
         ('SOF/DAC', 'SOF/DAC'),
         ('SOF/DAC/RBV', 'SOF/DAC/RBV'),
         ('SIM/SOF', 'SIM/SOF'),
         ('SOF/SIM/DAC/RBV', 'SOF/SIM/DAC/RBV'),
         ('SOF/SIM/DAC', 'SOF/SIM/DAC'),
         ('PAR/OMB', 'PAR/OMB'),
         ('PAR/OMB/RBV', 'PAR/OMB/RBV'),
         ('INF/RBV', 'INFRBV'),
         ('SOF/PAR/OMP', 'SOF/PAR/OMP'),
         ('PAR/OMB/RBV', 'PAR/OMB/RBV'),
         ('SOF/PAR/OMB/RBV', 'SOF/PAR/OMB/RBV'),
         ('SOF/VEL', 'SOF/VEL'),
         ('SOF/VEL/RBV', 'SOF/VEL/RBV'),
         ('SOF/VEL/VOX', 'SOF/VEL/VOX'),
         ('SOF/VEL/VOX/RBV', 'SOF/VEL/VOX/RBV'),
         ('SOF/LED/RBV', 'SOF/LED/RBV'),
         ('Wait', 'Wait'),
         ('Exclude', 'Exclude'),
         ('No Treatment', 'No Treatment'),
     )

    Final_Decision = models.CharField(
         choices=Final_Decision_Choices, max_length=200,null=True,blank=True)
    phyName = models.ForeignKey(phy,null = True,blank=True,on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.National_ID)
    def get_absolute_url(self):
        return reverse ('home')
        #return reverse('patient-detail',kwargs={'National_ID':National_ID})















class W0(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w0s',unique=True)
     FollowUp_date=models.DateField(null=True,blank=True)
     PhysicianName=models.CharField(max_length=200, null=True,blank=True)
     date = models.DateField(null=True)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True,null=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True,null=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200,blank=True)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)

     #treatment W0
     Ribavirine_dose=models.FloatField(null=True, max_length=200,blank=True)
     INF_Dose=models.FloatField(null=True, max_length=200,blank=True)
     SOF_Dose =models.FloatField(null=True, max_length=200,blank=True)
     SIM_Dose =models.FloatField(null=True, max_length=200,blank=True)
     LED=models.FloatField(null=True, max_length=200,blank=True)
     DAC=models.FloatField(null=True, max_length=200,blank=True)
     PAR_OMB=models.FloatField(null=True, max_length=200,blank=True)
     additional =models.CharField(null=True, max_length=200,blank=True)
     Other = models.TextField(null=True, max_length=200,blank=True)
     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True,null=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,null=True,max_length=200,blank=True)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,null=True,max_length=200,blank=True)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)



     created_on = models.DateTimeField(auto_now_add=True,blank=True)

     def __str__(self):
         return '%s -%s' % (self.patient.National_ID,self.date)

     def get_absolute_url(self):
            return reverse ('home')










#######################################start W4#################################










class W4(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w4s',unique=True)
     FollowUp_date=models.DateField( null=True)
     PhysicianName=models.CharField(max_length=200, null=True)
     date = models.DateField( null=True)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True, null=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True, null=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,null=True,max_length=200,blank=True)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,null=True,max_length=200,blank=True)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )
     HCV_RNA_W4 = models.CharField(choices=Not_Done_Choise,max_length=100,blank=True, null=True)


     created_on = models.DateTimeField(auto_now_add=True, null=True)

     def __str__(self):
         return '%s -%s' % (self.patient.National_ID,self.date)

     def get_absolute_url(self):
            return reverse ('home')












####################################start W8####################################













class W8(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w8s',unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',null=True,blank=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200,blank=True)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,null=True,max_length=200,blank=True)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,null=True,max_length=200,blank=True)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )



     created_on = models.DateTimeField(auto_now_add=True,blank=True)

     def __str__(self):
         return '%s -%s' % (self.patient.National_ID,self.date)

     def get_absolute_url(self):
            return reverse ('home')
            #















##########################start W12








class W12(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w12s' ,unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,blank=True,null=True,max_length=200)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,blank=True,null=True,max_length=200)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     HCV_RNA_W12= models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_W12=models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_Value_12 =models.IntegerField(null=True,blank=True)



     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')












##########################start week 16###########################














class W16(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w16s',unique= True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200,blank=True)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,blank=True,null=True,max_length=200)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,blank=True,null=True,max_length=200)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )



     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')














####################start W20


















class W20(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w20s',unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound', null=True,blank=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,blank=True,null=True,max_length=200)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,blank=True,null=True,max_length=200)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )



     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')

########################w24

class W24(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w24s',unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True, null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200,blank=True)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,blank=True,null=True,max_length=200)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,blank=True,null=True,max_length=200)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     HCV_RNA_W24 = models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_W24=models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_Value_24 =models.IntegerField(null=True,blank=True)
     CD4_count_W24=models.IntegerField(null=True)



     created_on = models.DateTimeField(auto_now_add=True,blank=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')















######################start W28
















class W28(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w28s',unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True,blank=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',blank=True,null=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,blank=True,null=True,max_length=200)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,null=True,max_length=200,blank=True)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )



     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')












##########################start w36






class W36(models.Model):

     patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='w36s',unique=True)
     FollowUp_date=models.DateField(null=False)
     PhysicianName=models.CharField(max_length=200, null=False)
     date = models.DateField(null=False)
     P_N_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
     )
     YES_NO_choise = (
         ('Yes', 'Yes'),
         ('NO', 'NO'),
     )
     HCV_RNA = models.CharField(choices=P_N_Choise, null=True, max_length=200,blank=True)
     Quant = models.IntegerField(null=True,blank=True)
     Limit_OF_Det_IU_ml = models.IntegerField(null=True,blank=True)
     Weight_Kgm = models.IntegerField(null=True,blank=True)
     BP_mmHg=models.TextField(null=True, max_length=200,blank=True)

     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     ALT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     ALT_Result = models.CharField(null=True, max_length=200,blank=True)
     AST_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AST_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AST_Result = models.FloatField(null=True, max_length=200,blank=True)
     ALP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     ALP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     AFP_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     AFP_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Total_BILIRUBIN_mg_d = models.FloatField(null=True,blank=True)
     Indirect_Bilirubin_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     GGT_IU_L = models.FloatField(null=True, max_length=200,blank=True)
     GGT_ULN = models.FloatField(null=True, max_length=200,blank=True)
     Plateletsx10_3 = models.IntegerField(null=True,blank=True)
     WBCx10_3_mm_3 = models.FloatField(null=True)
     ANCx10_3_mm_3 = models.FloatField(null=True, max_length=200,blank=True)
     Albumin_g_dL = models.FloatField(null=True,blank=True)
     Hb_G_L = models.IntegerField(null=True,blank=True)
     INR = models.FloatField(null=True, max_length=200,blank=True)
     Creatine_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     Glucose_mg_dL = models.FloatField(null=True, max_length=200,blank=True)
     TSH = models.FloatField(null=True, max_length=200,blank=True)
     PC = models.FloatField(null=True, max_length=200,blank=True)
     HbA1c = models.FloatField(null=True, max_length=200,blank=True)
     #abdonomindal follow up
     Date_Ultrasound = models.DateField(verbose_name='date Ultasound',null=True,blank=True)
     Liver_choices = (
         ('Normal', 'Normal'),
         ('Abnormal Echopattern', 'Abnormal Echopattern'),
         ('Cirrhotic', 'Cirrhotic'),
     )
     Liver = models.CharField(choices=Liver_choices, max_length=200,null=True,blank=True)
     PV_choices = (
         ('Patent', 'Patent'),
         ('Thrombosed', 'Thrombosed'),
     )
     PV = models.CharField(choices=PV_choices, max_length=200,null=True,blank=True)
     PV_Dimeter_mm = models.FloatField(null=True, max_length=200,blank=True)
     Other_ultrasound = models.CharField(null=True, max_length=200,blank=True)
     Ascites = models.CharField(choices=YES_NO_choise, max_length=200,null=True,blank=True)
     Ascites_choices = (
          ('Mild-Moderate', 'Mild-Moderate'),
          ('Tense', 'Tense'),
          ('mild-moderate', 'mild-moderate'),
          )
     Ascites_IF_YES = models.CharField(choices=Ascites_choices, max_length=200,blank=True)
     Presence_Of_focal_Lesions = models.CharField(
          choices=YES_NO_choise, max_length=200,blank=True)
     If_Presence_Of_focal_Lesions_yes_number = models.CharField(
          null=True, max_length=200,blank=True)
     Diameter_Of_Largest_cm = models.FloatField(null=True, max_length=200,blank=True)

     sonographic_Appearance_Malignant_choices = (
          ('Yes', 'Yes'),
          ('No', 'No'),
          ('Suspicious', 'Suspicious'),
          )
     sonographic_Appearance_Malignant = models.CharField(
          choices=sonographic_Appearance_Malignant_choices, max_length=200,null=True,blank=True)
     Other_Comment_Ultrasound = models.TextField(null=True,blank=True)


     #Side Effect
     presence_of_Side_Effects =models.CharField(choices=YES_NO_choise,max_length=200,blank=True)
     If_Presence_Of_side_effect_yes_choise=(
          ('Amnesia','Amnesia'),
          ('Pseudo-flu syndrome','Pseudo-flu syndrome'),
          ('Hair loss','Hair loss'),
          ('Respiratory Disorder','Respiratory Disorder'),
          ('Psychological Disorders','Psychological Disorders'),
          ('RASH','RASH'),
          ('GI symptoms','GI symptoms'),
          ('Anemia','Anemia'),
          ('jaundice','jaundice'),
          ('Ascites','Ascites'),
          ('Encephalopathy','Encephalopathy'),
          ('Hematemesis','Hematemesis'),
          ('Others','Others'),

     )
     If_Presence_Of_side_effect_yes =models.CharField(choices=If_Presence_Of_side_effect_yes_choise,null=True,max_length=200,blank=True)
     spicify_side_Effects=models.CharField(null=True,max_length=600,blank=True)
     Decision_To_Choise=(
          ('Continue with the same Treatment','Continue with the same Treatment'),
          ('Stop Treatment','Stop Treatment'),
          ('Change Dose','Change Dose'),

     )
     Decision_To=models.CharField(choices=Decision_To_Choise,null=True,max_length=200,blank=True)
     New_Ribavirin_Dose = models.FloatField(null=True,max_length=4,blank=True)
     New_INF_Dose= models.FloatField(null=True,max_length=4,blank=True)
     additional_sideEffect=models.CharField(null=True,max_length=100,blank=True)
     Treatment_intrruption_options_choise=(
          ('Serious Adverse event','Serious Adverse event'),
          ('Too Many adverse events','Too Many adverse events'),
          ('Died','Died'),
          ('Others','Others'),

     )
     Stop_Treatment_Options =models.CharField(choices=Treatment_intrruption_options_choise,null=True,max_length=200,blank=True)
     Spicify_Stop_Treatment = models.TextField(null=True,max_length=1000,blank=True)
     Not_Done_Choise = (
         ('Negative', 'Negative'),
         ('Positive', 'Positive'),
         ('NOT DONE', 'NOT DONE'),
     )

     HCV_RNA_W36 = models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_W36=models.CharField(choices=Not_Done_Choise,max_length=100,blank=True)
     HIV_PCR_Value_36 =models.IntegerField(null=True,blank=True)
     CD4_count_W36=models.IntegerField(null=True,blank=True)


     created_on = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s -%s' % (self.patient.Patient_Name,self.date)

     def get_absolute_url(self):
            return reverse ('home')
