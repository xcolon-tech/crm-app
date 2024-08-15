from django.urls import path
from .views import LeadListView, LeadDetailView, DealListView, DealDetailView

urlpatterns = [
    path('leads/', LeadListView.as_view(), name='lead-list'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('deals/', DealListView.as_view(), name='deal-list'),
    path('deals/<int:pk>/', DealDetailView.as_view(), name='deal-detail'),
]