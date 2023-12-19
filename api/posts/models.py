from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField()
    
