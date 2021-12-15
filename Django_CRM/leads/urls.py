from django.contrib import admin
from django.urls import path
from .views import LeadDeleteView,LeadUpdateView, LeadListView, LeadDetailView, LeadCreateView

app_name = "leads"

urlpatterns = [
    path('',LeadListView.as_view(), name='home'),
    path('create/',LeadCreateView.as_view(), name='create-lead'),
    path('detail/<int:pk>/',LeadDetailView.as_view(), name='detail-lead'),
    path('delete/<int:pk>/',LeadDeleteView.as_view(), name='delete-lead'),
    path('update/<int:pk>/',LeadUpdateView.as_view(), name='update-lead'),
   
]
 