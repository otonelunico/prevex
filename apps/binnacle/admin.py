from django.contrib import admin
from apps.binnacle.models import Accident,Area,Type_Accident,Workstation,Working


# Register your models here.

admin.site.register(Area)
admin.site.register(Accident)
admin.site.register(Type_Accident)
admin.site.register(Working)
admin.site.register(Workstation)