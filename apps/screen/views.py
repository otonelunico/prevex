from django.shortcuts import render, redirect
from apps.binnacle.models import Accident, Type_Accident
from apps.screen.models import Prevent, Video
from apps.screen.forms import PreventForm, VideoForm
from django.db.models import Count
import time
# Create your views here.


def index(request):
    data = {}
    data['screencast'] = 'active'
    current = Current()
    id_=current['id']
    print(id_)
    if id_ == 0:
        current = Current_day()
        id_=current['id']
    if id_ == 0:
        current = Current_mes()
        id_=current['id']
    print(id_)
    data['type']= Type_Accident.objects.get(id=id_)
    if Video.objects.filter(type=id_):
        data['video']= Video.objects.get(type=id_)

    data['Prevent']= Prevent.objects.filter(type=id_)
    print(data['type'])
    return render(request, 'screen/index.html', data)

def dia(value):
    dia = {1: 'Lunes',
           2: 'Martes',
           3: 'Miercoles',
           4: 'Jueves',
           5: 'Viernes',
           6: 'Sabado',
           7: 'Domingo'}
    return dia[value]

def Current():
    filter_one = {}
    now_day = time.strftime("%w")
    now_hour = time.strftime("%H")
    filter_one['total'] =0
    filter_one['id'] = 0
    for types in Type_Accident.objects.all().order_by('id'):
        model = Accident.objects.filter(type=types.id)
        cont = 0
        for llo in model:
            day = llo.date.strftime("%w")
            hour = llo.hour.strftime("%H")
            if now_day == day and now_hour == hour:
                cont = cont+1
            if cont > filter_one['total']:
                filter_one['total']=cont
                filter_one['title']= llo.type.title
                filter_one['id']= llo.type.id
    print(filter_one)
    return filter_one
def Current_day():
    filter_one = {}
    now_day = time.strftime("%w")
    filter_one['total'] =0

    filter_one['id'] = 0
    for types in Type_Accident.objects.all().order_by('id'):
        model = Accident.objects.filter(type=types.id)
        cont = 0
        for llo in model:
            day = llo.date.strftime("%w")
            if now_day == day:
                cont = cont+1
            if cont > filter_one['total']:
                filter_one['total']=cont
                filter_one['title']= llo.type.title
                filter_one['id']= llo.type.id
    return filter_one

def Current_mes():
    filter_one = {}
    now_day = time.strftime("%B")
    filter_one['total'] =0

    filter_one['id'] = 0
    for types in Type_Accident.objects.all().order_by('id'):
        model = Accident.objects.filter(type=types.id)
        cont = 0
        for llo in model:
            day = llo.date.strftime("%B")
            if now_day == day:
                cont = cont+1
            if cont > filter_one['total']:
                filter_one['total']=cont
                filter_one['title']= llo.type.title
                filter_one['id']= llo.type.id
    return filter_one

def Settings(request):
    data = {}
    data['screen'] = 'active'
    data['title'] = 'Configurar pantalla'
    data['option'] = 'Configurar pantalla'
    data['type'] =Type_Accident.objects.all().order_by('id')

    return render(request, 'screen/settings.html', data)

def Prevent_(request, funct, type, id):
    data = {}
    data['screen'] = 'active'
    id_int = int(id)
    data['model'] = Prevent.objects.filter(type=type)
    data['type'] = type
    if Video.objects.filter(type=type):
        data['video'] = Video.objects.get(type=type).url

    data['title'] = 'como prevenir '+ Type_Accident.objects.get(id=type).title
    if funct == 'create':
        data['form'] = PreventForm(request.POST)
        if request.method == 'POST':
            if data['form'].is_valid():
                data['form'].save()
    elif funct == 'edit':
        data['edit'] = Prevent.objects.get(id=id_int)
        if request.method == "GET":
            data['form'] = PreventForm(instance=data['edit'])
            print(data['form'])
        else:
            data['form'] = PreventForm(request.POST, instance=data['edit'])
            if data['form'].is_valid():
                data['form'].save()
            return redirect('screen:prevent', 'create', type, '0')
    elif funct == 'delete':
        Prevent.objects.get(id=id_int).delete()
        return redirect('screen:prevent', 'create', type, '0')
    return render(request, 'screen/prevent.html', data)

def Video_(request,funct, type):
    data = {}
    data['screen'] = 'active'
    data['type'] = type
    data['title']= Type_Accident.objects.get(id=type).title
    if funct == 'create':
        data['form'] = VideoForm(request.POST)
        if request.method == 'POST':
            if data['form'].is_valid():
                obj = data['form'].save(commit=False)
                obj.id =1
                data['form'].save()
                return redirect('screen:prevent', 'create', type, '0')
            else:
                print(data['form'].is_valid())
                print(data['form'].errors)

    elif funct == 'edit':
        data['edit'] = Video.objects.get(type=type)
        if request.method == "GET":
            data['form'] = VideoForm(instance=data['edit'])
            print(data['form'])
        else:
            data['form'] = VideoForm(request.POST, instance=data['edit'])
            if data['form'].is_valid():
                data['form'].save()
            return redirect('screen:prevent', 'create', type, '0')
    elif funct == 'delete':
        Video.objects.get(type=type).delete()
        return redirect('screen:prevent', 'create', type, '0')
    return render(request, 'screen/video.html', data)