from django.shortcuts import render

def list(request):
    return render(request, 'control/list.html', {})

def login(request):
    return render(request, 'control/login.html')
