from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(null=False, max_length=50)
    def __str__(self):
        return '{}'.format(self.title)

class Group(models.Model):
    title = models.CharField(null=False, max_length=50)
    def __str__(self):
        return '{}'.format(self.title)

class State(models.Model):
    title = models.CharField(null=False, max_length=50)
    def __str__(self):
        return '{}'.format(self.title)

class Item(models.Model):
    code = models.IntegerField(null=False, unique=True)
    description = models.CharField(max_length=50)
    group = models.ForeignKey(Group, null=False, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.code)

class Movement(models.Model):
    code = models.ForeignKey(Item, null=False, blank=True, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=False, blank=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=False, blank=True, on_delete=models.CASCADE)
    stock = models.IntegerField(null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.code)