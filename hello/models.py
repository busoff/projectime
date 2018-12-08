from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class ProjectTimeEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hour = models.FloatField('project hour', validators=(MinValueValidator(0.5), MaxValueValidator(24))) 
    date = models.DateField('date')

    def __str__(self):
        return '{}@{} on {}: {}'.format(self.user, self.project, self.date, self.hour)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    myid = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return "{} ({})".format(self.user.username, self.myid)
