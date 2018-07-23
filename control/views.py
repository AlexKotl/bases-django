from django.shortcuts import render
from bases.models import Base, Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from bases.settings_private import *

def list(request):
    if not 'access_level' in request.session:
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'control/list.html', {})

def login(request):
    return render(request, 'control/login.html')

def auth(request):
    if True:
        request.session['access_level'] = 1
    return HttpResponseRedirect(reverse('list'))
