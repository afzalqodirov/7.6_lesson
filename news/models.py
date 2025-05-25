from django.db import models

class New(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
