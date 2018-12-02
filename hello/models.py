from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField("User name", max_length=64)

    def __str__(self):
        return self.name

class ProjectTimeEntry(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hour = models.FloatField('project hour', validators=(MinValueValidator(0.5), MaxValueValidator(24))) 
    date = models.DateField('date')

    def __str__(self):
        return '{}@{} on {}: {}'.format(self.user, self.project, self.date, self.hour)



