from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'Role/index.html')

def addRole(request):

    return render(request, 'Role/addRole.html')


def edirRole(request):

    return render(request, 'Role/editRole.html')
