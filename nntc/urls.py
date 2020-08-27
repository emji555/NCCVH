
from django.urls import path
from . import views
from .views import HomeView,PatientDetailView,AddNewPatientView,UpdatePatientView,DeletePatientView,AddNewW0tView,AddNewW4tView,AddNewW8tView,AddNewW12tView,AddNewW16tView,AddNewW20tView,AddNewW24tView,AddNewW28tView,AddNewW36tView,UpdateW0,UpdateW4,UpdateW8,UpdateW12,UpdateW16,UpdateW20,UpdateW24,UpdateW28,UpdateW36,SearchResultsView, get_data,PhyView,DeletePhyView,UpdatephyView,AddNewPhyView
urlpatterns = [
   # path('',views.home,name="home")

   path('',HomeView.as_view(),name="home"),
   path('search/', SearchResultsView.as_view(), name='search_results'),
   path('patientView/<int:pk>',PatientDetailView.as_view(),name='patient-detail'),
   path('add_patient/',AddNewPatientView.as_view(),name='add_patient'),
   path('patientView/edit/<int:pk>',UpdatePatientView.as_view(),name='update_patient'),
   path('DeleteView/<int:pk>/remove',DeletePatientView.as_view(),name='delete_patient'),
   path('patientView/<int:pk>/followupw0/',AddNewW0tView.as_view(),name='add_w0'),
   path('patientView/<int:pk>/followupw4/',AddNewW4tView.as_view(),name='add_w4'),
   path('patientView/<int:pk>/followupw8/',AddNewW8tView.as_view(),name='add_w8'),
   path('patientView/<int:pk>/followupw12/',AddNewW12tView.as_view(),name='add_w12'),
   path('patientView/<int:pk>/followupw16/',AddNewW16tView.as_view(),name='add_w16'),
   path('patientView/<int:pk>/followupw20/',AddNewW20tView.as_view(),name='add_w20'),
   path('patientView/<int:pk>/followupw24/',AddNewW24tView.as_view(),name='add_w24'),
   path('patientView/<int:pk>/followupw28/',AddNewW28tView.as_view(),name='add_w28'),
   path('patientView/<int:pk>/followupw36/',AddNewW36tView.as_view(),name='add_w36'),
   path('patientView/W0View/edit/<int:pk>',UpdateW0.as_view(),name='update_W0'),
   path('patientView/W4View/edit/<int:pk>',UpdateW4.as_view(),name='update_W4'),
   path('patientView/W8View/edit/<int:pk>',UpdateW8.as_view(),name='update_W8'),
   path('patientView/W12View/edit/<int:pk>',UpdateW12.as_view(),name='update_W12'),
   path('patientView/W16View/edit/<int:pk>',UpdateW16.as_view(),name='update_W16'),
   path('patientView/W20View/edit/<int:pk>',UpdateW20.as_view(),name='update_W20'),
   path('patientView/W24View/edit/<int:pk>',UpdateW24.as_view(),name='update_W24'),
   path('patientView/W28View/edit/<int:pk>',UpdateW28.as_view(),name='update_W28'),
   path('patientView/W36View/edit/<int:pk>',UpdateW36.as_view(),name='update_W36'),
   path('index',views.index,name ='index'),
   path('api/data/',get_data,name = 'api-data'),
   #path('api/chart/data/',ChartsData.as_view()),
   path('phylist/',PhyView.as_view(),name='phyView'),
   path('add_physician/',AddNewPhyView.as_view(),name='add_physician'),


 #  path('data', views.pivot_data, name='pivot_data'),
 #  path('Center/<str:cents>/',CenterView,name = 'center'),
]
