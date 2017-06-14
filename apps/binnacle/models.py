from django.db import models

# Create your models here.

class Area(models.Model):
    title = models.CharField(null=False, max_length=50)
    detail = models.CharField(null=False, max_length=200)
    def __str__(self):
        return '{}'.format(self.title)

class Workstation(models.Model):
    title = models.CharField(null=False, max_length=50)
    detail = models.CharField(null=False, max_length=200)
    def __str__(self):
        return '{}'.format(self.title)

class Working(models.Model):
    name = models.CharField(null=False, max_length=50)
    workstation = models.ForeignKey(Workstation, null=False, blank=True, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=False, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.name+' - '+self.workstation.title+' - '+self.area.title)

class Type_Accident(models.Model):
    title = models.CharField(null=False, max_length=50)
    detail = models.CharField(null=False, max_length=200)
    def __str__(self):
        return '{}'.format(self.title)

class Accident(models.Model):
    working = models.ForeignKey(Working, null=False, blank=True, on_delete=models.CASCADE)
    year  = models.IntegerField(null=False)
    date = models.DateField(null=False)
    hour = models.TimeField(null=False)
    type = models.ForeignKey(Type_Accident, null=False, blank=True, on_delete=models.CASCADE)
    description = models.TextField(null=False)
    observation = models.CharField(max_length=100)
    area = models.ForeignKey(Area, null=False, blank=True, on_delete=models.CASCADE)
    workstation = models.ForeignKey(Workstation, null=False, blank=True, on_delete=models.CASCADE)
    repose = models.IntegerField()



