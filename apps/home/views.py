from django.shortcuts import render
from apps.user.views import Admin
from apps.inventory.models import Movement, Item
from apps.binnacle.models import Accident, Type_Accident
from django.contrib.auth.models import User
from datetime import date, datetime

# Create your views here.

def index(request):
    data = {}
    data['admin'] = Admin(request)
    data['home'] = 'active'
    data['cant']={
        'accident': Accident.objects.all().count(),
        'users' : User.objects.all().count(),
        'inventory': Item.objects.all().count(),
        'type_accident' : Type_Accident.objects.all().count()
    }
    data['inventory']= Movement.objects.all().order_by("-id")[:5]
    data['binnacle']= Accident.objects.all().order_by("-id")[:5]
    data['user_']= User.objects.filter(is_superuser=False).order_by("-id")[:5]
    data['last_accident']= Accident.objects.last()
    formato_fecha = "%Y-%m-%d"
    fecha_inicial = datetime.strptime(str(data['last_accident'].date), formato_fecha)
    fecha_final = datetime.now()
    data['days'] = fecha_final - fecha_inicial


    return render(request, 'home/index.html', data)

def Verify(request):
    return render(request, 'home/verifyforzoho.html')