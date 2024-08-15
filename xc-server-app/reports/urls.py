from django.urls import path
from .views import (
    SalesReportListView, SalesReportDetailView,
    CustomerReportListView, CustomerReportDetailView,
    MarketingReportListView, MarketingReportDetailView
)

urlpatterns = [
    # Sales Reports
    path('sales-reports/', SalesReportListView.as_view(), name='sales-report-list'),
    path('sales-reports/<int:pk>/', SalesReportDetailView.as_view(), name='sales-report-detail'),
    
    # Customer Reports
    path('customer-reports/', CustomerReportListView.as_view(), name='customer-report-list'),
    path('customer-reports/<int:pk>/', CustomerReportDetailView.as_view(), name='customer-report-detail'),
    
    # Marketing Reports
    path('marketing-reports/', MarketingReportListView.as_view(), name='marketing-report-list'),
    path('marketing-reports/<int:pk>/', MarketingReportDetailView.as_view(), name='marketing-report-detail'),
]