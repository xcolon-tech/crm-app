from rest_framework import serializers
from .models import SalesReport, CustomerReport, MarketingReport

class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReport
        fields = '__all__'

class CustomerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReport
        fields = '__all__'

class MarketingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingReport
        fields = '__all__'