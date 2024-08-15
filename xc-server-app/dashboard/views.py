from rest_framework import generics
from .models import Lead, Deal
from .serializers import LeadSerializer, DealSerializer

class LeadListView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class DealListView(generics.ListCreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer