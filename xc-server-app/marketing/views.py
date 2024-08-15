from rest_framework import generics
from .models import MarketingCampaign
from .serializers import MarketingCampaignSerializer

class MarketingCampaignListView(generics.ListCreateAPIView):
    queryset = MarketingCampaign.objects.all()
    serializer_class = MarketingCampaignSerializer

class MarketingCampaignDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketingCampaign.objects.all()
    serializer_class = MarketingCampaignSerializer