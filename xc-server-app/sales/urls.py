from django.urls import path
from .views import SalesOpportunityListView, SalesOpportunityDetailView

urlpatterns = [
    path('sales-opportunities/', SalesOpportunityListView.as_view(), name='sales-opportunity-list'),
    path('sales-opportunities/<int:pk>/', SalesOpportunityDetailView.as_view(), name='sales-opportunity-detail'),
]