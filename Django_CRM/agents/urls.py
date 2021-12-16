from django.contrib import admin
from django.urls import path
from .views import AgentListView

app_name = "agents"

urlpatterns = [
     path('',AgentListView.as_view(), name='agent'),
    # path('create/',LeadCreateView.as_view(), name='create-lead'),
    # path('detail/<int:pk>/',LeadDetailView.as_view(), name='detail-lead'),
    # path('delete/<int:pk>/',LeadDeleteView.as_view(), name='delete-lead'),
    # path('update/<int:pk>/',LeadUpdateView.as_view(), name='update-lead'),
   
]
 