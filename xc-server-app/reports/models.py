from django.db import models

class Report(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class SalesReport(Report):
    pass

class CustomerReport(Report):
    pass

class MarketingReport(Report):
    pass