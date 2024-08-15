from rest_framework import serializers
from .models import MarketingCampaign

class MarketingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingCampaign
        fields = '__all__'