from django.urls import path
from .views import LeadListView, LeadDetailView

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
]