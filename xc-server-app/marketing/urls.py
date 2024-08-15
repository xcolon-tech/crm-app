from django.urls import path
from .views import MarketingCampaignListView, MarketingCampaignDetailView

urlpatterns = [
    path('marketing-campaigns/', MarketingCampaignListView.as_view(), name='marketing-campaign-list'),
    path('marketing-campaigns/<int:pk>/', MarketingCampaignDetailView.as_view(), name='marketing-campaign-detail'),
]