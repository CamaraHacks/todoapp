from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    
    PRIORITY_CHOICES = [
    ('low', '🟢 Baixa'),
    ('medium', '🟡 Média'), 
    ('high', '🔴 Alta'),
    ('urgent', '⚡ Urgente'),
    ]

    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(
            max_length=200,
            choices=PRIORITY_CHOICES,
            default='medium')
    
    class Meta:
        ordering = ['completed','created_date']
