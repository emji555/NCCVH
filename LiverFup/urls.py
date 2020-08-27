
from django.urls import path
from .views import LiverList , LiverPDetailView,AddNewLiverPView
from . import views



urlpatterns = [
    path('LiverList/',LiverList.as_view(), name ='LiverList'),
    path('inrollmentView/<int:pk>',LiverPDetailView.as_view(),name='inrollment-detail'),

    path('add_liverp/',AddNewLiverPView.as_view(),name='add_liverp'),


    ]
