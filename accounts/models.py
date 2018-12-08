from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    myid = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return "{} ({})".format(self.user.username, self.myid)
