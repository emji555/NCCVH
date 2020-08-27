
from django.shortcuts import render , get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView, DeleteView
from  nntc.models import Patient ,Profile ,W0,W4,W8,W12,W16,W20,W24,W28,W36 ,phy
from .forms import PatientForm,EditPatientForm , W0Form , W4Form , W8Form , W12Form , W16Form ,W20Form ,W24Form,W28Form,W36Form,W0FormUpdate,W4FormUpdate,W8FormUpdate,W12FormUpdate,W16FormUpdate,W20FormUpdate,W24FormUpdate,W28FormUpdate,W36FormUpdate,phyForm,EditPhyForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.views import View , generic
from django.contrib.auth.decorators import permission_required
from django .contrib import messages
from reportlab.pdfgen import canvas
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
import csv , io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import JsonResponse
from django.core import serializers , paginator

##################API VIEW CHART ##################33
# User = get_user_model()
# class ChartsData(APIView):

#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         data = {
#              "sales":100,
#              "costumer":10,
#              "users": User.objects.all().count()
#             }
#         return Response(data)
#def Patient_with_pivot(request):
 #   return render(request,'dashboard_with_pivot.html',{})
#def pivot_data(request):
 #   dataset = Patient.objects.all()
  #  data =serializers.Serializer('jason',dataset)
   # return JsonResponse(data,safe=False)
# Create your views here.
#def home(request):
 #   return render(request,'home.html',{})
class homeviews(View):
    def get(self, request, *args, **kwargs):
        return render(request,'charts.html',{})
def get_data(request,*args,**kwargs):
    data = {
        "sales":100,
        "costumer":10,
    }
    return JsonResponse(data)
def index(request):
    """View function for home page of site."""
# Generate counts of some of the main objects
    num_patient = Patient.objects.all().count()





    num_Male = Patient.objects.filter(gender__exact='Male').count()
    num_Female = Patient.objects.filter(gender__exact='Female').count()
    num_patient_Center = Patient.objects.filter(Center_ID=2).count()

#



    context = {
        'num_patient': num_patient,

        'num_Male': num_Male,
        'num_Female': num_Female,

    }

    return render(request, 'index.html', context=context)


class HomeView(generic.ListView):
    model= Patient
    template_name = 'home.html'
    #paginator = paginator(patients,3)
    ordering =['-created_on']
    paginate_by = 10










#def CenterView(request,cents):
 #   center_patients = Patient.objects.filter(Center_ID=cents)
  #  return render(request,'center.html',{'cents':cents,'center_patients':center_patients})

class PatientDetailView(DetailView):
    model =Patient
    template_name ='patient_detail.html'

class AddNewPatientView(CreateView):
    model=Patient
    form_class =PatientForm
    template_name ='add_patient.html'
    #fields='__all__'

        ###########################################follow up start add here
class AddNewW0tView(CreateView):
    model=W0
    form_class =W0Form
    template_name ='add_wo.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class AddNewW4tView(CreateView):
    model=W4
    form_class =W4Form
    template_name ='add_w4.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class AddNewW8tView(CreateView):
    model=W8
    form_class =W8Form
    template_name ='add_w8.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')


class AddNewW12tView(CreateView):
    model=W12
    form_class =W12Form
    template_name ='add_w12.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class AddNewW16tView(CreateView):
    model=W16
    form_class =W16Form
    template_name ='add_w16.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class AddNewW20tView(CreateView):
    model=W16
    form_class =W20Form
    template_name ='add_w20.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class AddNewW24tView(CreateView):
    model=W24
    form_class =W24Form
    template_name ='add_w24.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class AddNewW28tView(CreateView):
    model=W24
    form_class =W28Form
    template_name ='add_w28.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

class AddNewW36tView(CreateView):
    model=W36
    form_class =W36Form
    template_name ='add_w36.html'
   # fields='__all__'
    def form_valid(self,form):
        form.instance.patient_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

   ##############################################   end add follow up
class UpdateW0(UpdateView):
    model= W0
    form_class =W0FormUpdate
    template_name = 'update_W0.html'



class UpdateW4(UpdateView):
    model= W4
    form_class =W4FormUpdate
    template_name = 'update_W4.html'


class UpdateW8(UpdateView):
    model= W8
    form_class =W8FormUpdate
    template_name = 'update_W8.html'


class UpdateW12(UpdateView):
    model= W12
    form_class =W12FormUpdate
    template_name = 'update_W12.html'

class UpdateW16(UpdateView):
    model= W16
    form_class =W16FormUpdate
    template_name = 'update_W16.html'

class UpdateW20(UpdateView):
    model= W20
    form_class =W20FormUpdate
    template_name = 'update_W20.html'

class UpdateW24(UpdateView):
    model= W24
    form_class =W24FormUpdate
    template_name = 'update_W24.html'

class UpdateW28(UpdateView):
    model= W28
    form_class =W28FormUpdate
    template_name = 'update_W28.html'
class UpdateW36(UpdateView):
    model= W36
    form_class =W36FormUpdate
    template_name = 'update_W36.html'

#####################################################end Update follow up #######################################
class UpdatePatientView(UpdateView):
    model= Patient
    form_class =EditPatientForm
    template_name = 'update_patient.html'

class DeletePatientView(DeleteView):
    model = Patient
    template_name ='delete_patient.html'
    success_url = reverse_lazy('home')


#sreach function

from django.db.models import Q
class SearchResultsView(ListView):
    model = Patient
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(
            Q(National_ID__icontains=query) | Q(Patient_Name__icontains=query)
        )
        return object_list
##################### Phytions#####################
class AddNewPhyView(CreateView):
    model=Patient
    form_class =phyForm
    template_name ='add_phy.html'
    #fields='__all__'


class PhyView(generic.ListView):
    model= phy
    template_name = 'phyList.html'
    #paginator = paginator(patients,3)
    #ordering =['-created_on']
    paginate_by = 10

class DeletePhyView(DeleteView):
    model = phy
    template_name ='delete_phy.html'
    success_url = reverse_lazy('home')

class UpdatephyView(UpdateView):
    model= Patient
    form_class =EditPhyForm
    template_name = 'update_phy.html'
