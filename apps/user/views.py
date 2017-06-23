from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
#from apps.user.models import Group, User_group
from django.views.generic import ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


from apps.user.forms import AuthForm


# Create your views here.

def Registeruser(request):

    data = {}
    data['adminuser'] = 'active'
    data['admin']= Admin(request)
    data['form'] = AuthForm
    data['groups'] = Group.objects.all().order_by('-id')
    print()
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            group = Group.objects.get(name='Usuario')
            user = User.objects.last()
            user.groups.add(group)
            return redirect('user:list')
        else:
            print(form.is_valid())
            print(form.errors)
    return render(request, 'auth/user_form.html', data)

def Admin(request):
    group = Group.objects.get(name='Administrador')
    for lo in User.objects.filter(groups__name=group.name):

        for un in User.objects.all():
            if un == lo :
                print(un.id)
                print(request.user.id)
                if un.id == request.user.id:
                    print('true')
                    return True
                else:
                    print('false')
                    return False

def Listuser(request):
    data={}

    data['adminuser'] = 'active'
    data['admin']= Admin(request)
    group = Group.objects.all()
    users = User.objects.all().order_by('username')
    data['users']={}
    for ll in group:
        for lo in User.objects.filter(groups__name=ll).order_by('username'):
            for un in users:
                if un == lo and un.is_superuser == False:
                    data['users'][un.username]={
                        'id': un.id,
                        'username': un.username,
                        'first_name':un.first_name,
                        'last_name':un.last_name,
                        'email':un.email,
                        'group': ll,
                        'is_active': un.is_active
                    }
    return render(request, 'auth/user_list.html', data)

def Deactivate(request, id):
    user = User.objects.get(id=id)
    user.is_active= False
    user.save()
    return redirect('user:list')

def Activate(request, id):
    user = User.objects.get(id=id)
    user.is_active= True
    user.save()
    return redirect('user:list')

def Editaccount(request, id):
    data={}
    data['admin'] = Admin(request)
    data['adminuser'] = 'active'

    id_=int(id)
    if id_==0:
        id_= request.user.id
    obj=User.objects.get(id=id_)
    if request.method == "GET":
        data['form'] = AuthForm(instance=obj)
        data['user_'] = obj
    else:
        data['form'] = AuthForm(request.POST, instance=obj)
        if data['form'].is_valid():
            data['form'].save()
            if id_ == request.user.id:
                return redirect('logout')
            else:
                return redirect('user:list')
        else:
            print(data['form'].is_valid())
            print(data['form'].errors)
    return render(request, 'auth/user_form.html', data)

def Edit_type(request, id, type):
    user=User.objects.get(id = id)
    if type == 'Usuario':
        type_new = 'Administrador'
        type_old = 'Usuario'
    else:
        type_new = 'Usuario'
        type_old = 'Administrador'
    group_new = Group.objects.get(name=type_new)
    group_old = Group.objects.get(name=type_old)
    user.groups.remove(group_old)
    user.groups.add(group_new)
    user.save()
    return redirect('user:list')
