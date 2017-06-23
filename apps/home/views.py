from django.shortcuts import render
from apps.user.views import Admin

# Create your views here.

def index(request):
    data = {}
    data['admin'] = Admin(request)
    data['home'] = 'active'
    return render(request, 'home/index.html', data)

def Verify(request):
    return render(request, 'home/verifyforzoho.html')