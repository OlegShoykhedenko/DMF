from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    TASK_STATE = (
        ('TODO', 'TODO'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False)
    task_state = models.CharField(max_length=12, choices=TASK_STATE, default=TASK_STATE[0][0])
   
    def __str__(self):
        return self.title
 