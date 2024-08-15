from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=50, choices=[('New', 'New'), ('Contacted', 'Contacted'), ('Qualified', 'Qualified'), ('Lost', 'Lost')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name