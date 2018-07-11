from captcha import captcha
from bases.models import Base, Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def add_submit(request):
    return HttpResponseRedirect(reverse('add_done'))

def add_done(request):
    return render(request, 'bases/add_done.html', {})

def add(request):
    return render(request, 'bases/add.html', {
        'sys_message': request.GET.get('message')
    })
