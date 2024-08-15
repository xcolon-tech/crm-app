from rest_framework import generics
from .models import SalesOpportunity
from .serializers import SalesOpportunitySerializer

class SalesOpportunityListView(generics.ListCreateAPIView):
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer

class SalesOpportunityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesOpportunity.objects.all()
    serializer_class = SalesOpportunitySerializer