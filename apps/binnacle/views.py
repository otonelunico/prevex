from django.shortcuts import render, redirect
from apps.binnacle.models import Area, Accident, Workstation, Working, Type_Accident
from apps.binnacle.forms import WorkingForm, WorkstationForm,  AreaForm, AccidentForm, Type_AccidentForm
from django.db.models import Count
from apps.user.views import Admin
from django.contrib.auth.models import User

import os

# Create your views here.

def index(request):
    data = {}
    data['admin'] = Admin(request)
    data['binnacle'] = 'active'
    data['model'] = Accident.objects.all().order_by('-id')[:5]
    data['accidentados'] = Accident.objects.all().aggregate(Count('id'))
    data['accidentados'] = data['accidentados']['id__count']
    repose = 0
    for item in Accident.objects.all():
        if item.repose != 0:
            repose =repose +1
    data['repose']=repose
    return render(request, 'binnacle/index.html', data)

def All_accident(request):
    data = {}
    data['admin'] = Admin(request)
    data['binnacle'] = 'active'
    data['model'] = Accident.objects.all().order_by('-id')
    return render(request, 'binnacle/all_accident.html', data)

def All_repose(request):
    data = {}
    data['admin'] = Admin(request)
    data['binnacle'] = 'active'
    data['model']={}
    llo = Accident.objects.filter().order_by('-id')
    for llos in llo:
        if llos.repose != 0:
            data['model'][llos]=llos

    return render(request, 'binnacle/all_accident.html', data)

def Create_value(request, value, funct, id):
    data = { 'binnacle': 'active'}
    data['admin'] = Admin(request)
    data['value'] = value
    id_int = int(id)
    form = {}
    if value == 'workstation':
        data['model'] = Workstation.objects.all().order_by('title')
        data['title'] = 'puesto de trabajo'
        if funct == 'create':
            form = WorkstationForm(request.POST)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
        elif funct == 'edit':
            data['edit'] = Workstation.objects.get(id=id_int)
            if request.method == "GET":
                data['form'] = WorkstationForm(instance=data['edit'])
                print(data['form'])
            else:
                form = WorkstationForm(request.POST, instance=data['edit'])
                if form.is_valid():
                    form.save()
                return redirect('binnacle:create_value', value, 'create', '0')
    elif value == 'area':
        data['model'] = Area.objects.all().order_by('title')
        data['title'] = 'area de trabajo'
        if funct == 'create':
            form = AreaForm(request.POST)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
        elif funct == 'edit':
            data['edit'] = Area.objects.get(id=id_int)
            if request.method == "GET":
                data['form'] = AreaForm(instance=data['edit'])
                print(data['form'])
            else:
                form = AreaForm(request.POST, instance=data['edit'])
                if form.is_valid():
                    form.save()
                return redirect('binnacle:create_value', value, 'create', '0')
    elif value == 'type':
        data['model'] = Type_Accident.objects.all().order_by('title')
        data['title'] = 'tipo de accidente'
        if funct == 'create':
            form = Type_AccidentForm(request.POST)
            if request.method == 'POST':
                if form.is_valid():
                    form.save()
        elif funct == 'edit':
            data['edit'] = Type_Accident.objects.get(id=id_int)
            if request.method == "GET":
                form = Type_AccidentForm(instance=data['edit'])

            else:
                form = Type_AccidentForm(request.POST, instance=data['edit'])
                if form.is_valid():
                    form.save()
                return redirect('binnacle:create_value', value, 'create', '0')
    return render(request, 'binnacle/create_value.html', data)

def Create_working(request, value):
    data = {'binnacle': 'active'}
    data['admin'] = Admin(request)
    data['model'] = Working.objects.all().order_by('name')
    value_int = int(value)
    if value_int == 0:
        data['area'] = Area.objects.all().order_by('title')
        data['workstation'] = Workstation.objects.all().order_by('title')
        data['form'] = WorkingForm()
        data['title'] = 'trabajador'
        if request.method == 'POST':
            form = WorkingForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('binnacle:working', value)
    return render(request, 'binnacle/working.html', data)

def Create_accident(request,funct, value):
    data = {'binnacle': 'active'}
    data['admin'] = Admin(request)
    data['model'] = Accident.objects.all()
    value_int = int(value)
    data['area'] = Area.objects.all().order_by('title')
    data['type'] = Type_Accident.objects.all().order_by('title')
    data['workstation'] = Workstation.objects.all().order_by('title')
    data['working'] = Working.objects.all().order_by('name')
    data['form'] = AccidentForm()
    data['title'] = 'accidente'
    if funct == 'create':
        if request.method == 'POST':
            form = AccidentForm(request.POST)
            if form.is_valid():
                form.save()
                Send(str(Accident.objects.last().id))
                return redirect('binnacle:index')
            else:
                print(form.is_valid())
                print(form.errors)
    elif funct == 'edit':
        data['edit']=Accident.objects.get(id=value_int)
        if request.method == 'POST':
            form = AccidentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('binnacle:index')
            else:
                print(form.is_valid())
                print(form.errors)
    elif funct == 'view':
        data['edit']=Accident.objects.get(id=value_int)
        data['view'] = 'disabled'
        if request.method == 'POST':
            form = AccidentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('binnacle:index')
            else:
                print(form.is_valid())
                print(form.errors)
    return render(request, 'binnacle/accident.html', data)


from django.core.mail import send_mail

def Notify(subject, message,receiver):
    send_mail(subject,
               message,
              "support@prevex.herokuapp.com",
              [receiver],
                fail_silently = False)
def Send(id):
    print('id del guardado es'+id)
    dominio = 'http://0.0.0.0:8888/'
    if os.getenv('SETTINGS_MODE') in ['PROD']:
        dominio = 'https://prevex.herokuapp.com/'
    email = User.objects.all().order_by('id')
    for llo in email:
        print(llo)
        Notify('Se a registrado un nuevo accidente',
               'Se a ingresado un nuevo accidente, haga clic en el siguiente enlace para ver detalles. '+dominio+'binnacle/accident/view/'+id,
               llo.email)
