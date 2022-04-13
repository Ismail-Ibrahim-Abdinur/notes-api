from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('unfinished', 'Unfinished'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    status= models.CharField(choices=STATUS_CHOICES, max_length=20, default='unfinished')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
