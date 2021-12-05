from django.db import models
from datetime import datetime    

# Create your models here.
class Calculator_histoty(models.Model):
    equation = models.CharField(max_length=25)
    result = models.CharField(max_length=25)
    date_added = models.DateTimeField(default=datetime.now, blank=True)


