from django.shortcuts import render, redirect
from apps.inventory.models import Movement, Location, State, Group, Item
from apps.inventory.forms import GroupForm, StateForm, LocationForm, ItemForm, MovementForm
from django.db.models import Sum


# Create your views here.

def index(request):
    model_item = Item.objects.all()
    data = {}
    data['inventory'] = 'active'
    data['title'] = 'Inventario'
    data['data'] = {}
    for items in model_item:
        items.sum = 0
        model_move = Movement.objects.filter(code=items)
        total = model_move.aggregate(Sum('stock'))
        if total['stock__sum']:
            items.sum = str(total['stock__sum'])
        else:
            items.sum = '0'

        data['data'][items]={'code': items.code,
                       'sum': items.sum,
                        'description': items.description,
                       'group': items.group.title}
    return render(request, 'inventory/index.html', data)


def Movement_maint(request, value, code):
    data = {}
    data['title'] = 'Inventario'
    data['inventory'] = 'active'
    if value == 'create':
        int_code = int(code)
        if code == '0':
            data['item'] = Item.objects.all()
            data['data'] = Movement.objects.all().order_by("-id")[:5]
        elif code != '0':
            data['select']= Item.objects.get(code = int_code)
            csl = True
            id_ = Item.objects.get(code=int_code)
            data['data'] = Movement.objects.filter(code = id_.id).order_by("-id")[:5]

        data['state'] = State.objects.all()
        data['location'] = Location.objects.all()
        data['form'] = MovementForm()
        data['code'] = code

        if request.method == 'POST':
            form = MovementForm(request.POST)
            if form.is_valid():
                form.save()

            return redirect('inventory:movement', 'create', code)

        #data['option_'] = MovementForm()
    return render(request, 'inventory/movement.html', data)


def Create_value(request, value):
    data = {}
    data['title'] = 'Inventario'
    data['group'] = {'model': Group.objects.all().order_by('title'), 'form': GroupForm, 'title': 'Grupo', 'inventory': 'active'}
    data['state'] = {'model': State.objects.all(), 'form': StateForm, 'title': 'Estado', 'inventory': 'active'}
    data['location'] = {'model': Location.objects.all(), 'form': LocationForm, 'title': 'Ubicacion', 'inventory': 'active'}
    if request.method == 'POST':
        form = data[value]['form'](request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:maintainer_item', 'create', '0')

    return render(request, 'inventory/create_value.html', data[value])


def Maintainer_item(request, value, code):
    data = {
        'data' : Item.objects.all(),
        'form' : ItemForm(),
        'group': Group.objects.all(),
        'option': 'Mantenedor de items'
    }
    data['inventory'] = 'active'
    data['title'] = 'Inventario'
    if value == 'create':
        data['model'] = Item.objects.all()
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('inventory:maintainer_item', 'create', '0')
            else:
                print(form.is_valid())
                print(form.errors)
    elif value == 'edit':
        code_=str(code)
        item = Item.objects.get(code=code_)
        data['form'] = ItemForm(instance=item)
        data['edit'] = Item.objects.get(code=code_)
        if request.method == "POST":
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
            return redirect('inventory:maintainer_item', 'create', '0')

    return render(request, 'inventory/maintainer_item.html', data)

def Movement_detail(request, code):
    int_code = int(code)
    id_ = Item.objects.get(code=int_code)
    data ={
        'obj' : id_,
        'model': Movement.objects.filter(code=id_.id).order_by("-id")
    }
    data['inventory'] = 'active'
    data['title'] = 'Inventario'
    return render(request, 'inventory/movement_detail.html', data)
