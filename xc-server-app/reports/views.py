from rest_framework import generics
from .models import SalesReport, CustomerReport, MarketingReport
from .serializers import SalesReportSerializer, CustomerReportSerializer, MarketingReportSerializer

class SalesReportListView(generics.ListCreateAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

class SalesReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

class CustomerReportListView(generics.ListCreateAPIView):
    queryset = CustomerReport.objects.all()
    serializer_class = CustomerReportSerializer

class CustomerReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerReport.objects.all()
    serializer_class = CustomerReportSerializer

class MarketingReportListView(generics.ListCreateAPIView):
    queryset = MarketingReport.objects.all()
    serializer_class = MarketingReportSerializer

class MarketingReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MarketingReport.objects.all()
    serializer_class = MarketingReportSerializer