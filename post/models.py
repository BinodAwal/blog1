from django.db import models

# Create your models here.

class post(models.Model):
    titles = models.CharField(max_length = 150)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    author = models.