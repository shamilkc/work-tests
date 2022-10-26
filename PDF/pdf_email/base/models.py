from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Files(models.Model):
    name = models.CharField(max_length = 200)
    file = models.FileField()

   
