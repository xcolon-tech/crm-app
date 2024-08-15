from django.db import models

class MarketingCampaign(models.Model):
    CAMPAIGN_TYPE_CHOICES = [
        ('Campaign', 'Campaign'),
        ('Social Media', 'Social Media'),
        ('Email', 'Email'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=CAMPAIGN_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.type})"