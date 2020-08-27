from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from  .models import inrollment ,Visit
from .forms import inrollmentForm
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect

# Create your views here.

class LiverList(ListView):
    model= inrollment
    template_name = 'LiverFup/LiverHome.html'
    ordering =['-created_on']
    paginate_by = 20

class LiverPDetailView(DetailView):
    model =inrollment
    template_name ='LiverFup/inrollment_detail.html'

class AddNewLiverPView(CreateView):
    model=inrollment
    form_class =inrollmentForm
    template_name ='LiverFup/add_lpatient.html'


        ###########################################follow up start add here
#class AddNewVisittView(CreateView):
 #   model=Visit
  #  form_class =VisitForm
   # template_name ='LiverFup/add_Visit.html'
   # fields='__all__'
#    def form_valid(self,form):
 #       form.instance.patient_id = self.kwargs['pk']
  #      return super().form_valid(form)
   # success_url = reverse_lazy('LiverList')
