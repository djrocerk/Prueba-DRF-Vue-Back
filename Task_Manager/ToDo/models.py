from django.db import models
from Users.models import Users

class Task(models.Model):
    TODO = 'todo'
    DONE = 'done'
    IN_PROGRESS = 'in progress'

    STATUS_CHOICES = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (IN_PROGRESS, 'In progress'),
    )

    description = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=TODO)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)