from django.db import models
from django.contrib.auth.models import User

class CFG_States(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(null=True)
    state = models.ForeignKey(CFG_States, related_name='state_fk', on_delete=models.PROTECT)
    details = models.TextField()

    def __str__(self):
        return self.title

