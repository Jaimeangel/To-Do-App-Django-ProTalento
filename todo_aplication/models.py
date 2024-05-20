from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user_id =models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    task=models.CharField(max_length=150)
    description=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)
    completed_task=models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.task

