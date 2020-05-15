from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Log(models.Model):
    date_posted = models.DateTimeField(default=timezone.now)
    worked_on = models.TextField()
    hours_spent = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

