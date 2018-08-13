from django.shortcuts import render
from bases.models import Base, Comments
from django.http import HttpResponseRedirect
from django.urls import reverse
from bases.settings_private import *
from .form import BaseForm

def check_access(request, required=0):
    ''' Checks for proper access level and redirects to login page '''
    if not 'access_level' in request.session or required > 0 and request.session.access_level != required:
        return False
    return True

def dashboard(request):
    if not check_access(request):
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'control/dashboard.html', {
        'bases': Base.objects.all(),
    })

def list(request):
    if not check_access(request):
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'control/list.html', {})

def edit_base(request, base_id):
    base = Base.objects.get(pk=base_id)
    return render(request, 'control/edit_base.html', {
        'base': base,
        'form': BaseForm(initial = {
            'address': base.address,
            'name': base.name,
            'contacts': base.contacts,
            'price': base.price,
            'description': base.description,
        }),
        'message': request.GET.get('message'),
    })

def save_base(request, base_id):
    base = Base.objects.get(pk=base_id)
    base.name = request.POST.get('name', '')
    base.contacts = request.POST.get('contacts', '')
    base.price = request.POST.get('price', 0)
    base.description = request.POST.get('description', '')
    base.save()

    return HttpResponseRedirect('%s?message=%s' % (reverse('edit_base', args=(base_id,)), "Изменения сохранены"))

def block_base(request, base_id):
    return HttpResponseRedirect(reverse('dashboard'))

def unblock_base(request, base_id):
    return HttpResponseRedirect(reverse('dashboard'))

def login(request):
    return render(request, 'control/login.html')

def remind(request):
    return render(request, 'control/remind.html')

def auth(request):
    # if admin
    if request.POST.get('login') == CMS_ADMIN_LOGIN and request.POST.get('password') == CMS_ADMIN_PASSWORD:
        request.session['access_level'] = 1
    return HttpResponseRedirect(reverse('dashboard'))

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('dashboard'))
