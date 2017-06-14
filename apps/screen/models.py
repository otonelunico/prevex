from django.db import models
from apps.binnacle.models import Type_Accident

# Create your models here.
class Prevent(models.Model):
    type = models.ForeignKey(Type_Accident, null=False, blank=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=300)
    def __str__(self):
        return '{}'.format(self.type)

class Video(models.Model):
    type = models.ForeignKey(Type_Accident, null=False, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)