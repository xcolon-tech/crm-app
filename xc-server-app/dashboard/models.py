from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)  # e.g., 'New', 'In Progress', etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Deal(models.Model):
    name = models.CharField(max_length=255)
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name='deals')
    status = models.CharField(max_length=255)  # e.g., 'Ongoing', 'Closed', etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name