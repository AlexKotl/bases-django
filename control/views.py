from django.shortcuts import render
from bases.models import Base, Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from bases.settings_private import *

def check_access(request, required=0):
    ''' Checks for proper access level and redirects to login page '''
    if not 'access_level' in request.session or required > 0 and request.session.access_level != required:
        return False
    return True

def list(request):
    if not check_access(request):
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'control/list.html', {})

def login(request):
    return render(request, 'control/login.html')

def auth(request):
    if True:
        request.session['access_level'] = 1
    return HttpResponseRedirect(reverse('list'))

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('list'))
