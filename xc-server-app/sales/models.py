from django.db import models

class SalesOpportunity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Closed', 'Closed')])
    close_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name