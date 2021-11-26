from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Job(models.Model):

    position_name       = models.CharField(max_length=100)
    text_description    = models.TextField()
    min_age             = models.IntegerField()
    max_age             = models.IntegerField()
    salary              = models.IntegerField() 
    n_openings          = models.IntegerField()
    creator             =models.ForeignKey(User,on_delete=models.CASCADE,default=None)

