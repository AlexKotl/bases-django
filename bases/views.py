import re
import urllib
import datetime
from captcha import captcha
from .models import Base, Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .settings_private import *

def map(request):
    bases = Base.get_all(request)
    bases_updated = []
    for base in bases:
        base.description = base.description.replace('"', '\"')
        base.description = re.sub('\s+', ' ', base.description)

        # define marker and z-index over map
        if base.rating >= 4 and base.votes >= 30:
            base.marker = 'images/markers/pointer_star.png'
            base.zindex = 3
        elif base.deltatime > 365 * 60*60*24:
            base.marker = 'images/markers/pointer_grey.png'
            base.zindex = 1
        else:
            base.marker = 'images/markers/pointer_red.png'
            base.zindex = 2

        bases_updated.append(base)

    return render(request, 'bases/map.html', {
        'bases': bases_updated,
        'bases_latest': Base.get_latest(request),
    })

def list(request):
    return render(request, 'bases/list.html', {
        'bases': Base.get_all(request),
    })

def details(request, base_name):
    base = Base.objects.get(url=base_name)
    return render(request, 'bases/details.html', {
        'base': base,
        'is_voted': 'is_rated_comment[{id}]'.format(id=base.id) in request.COOKIES,
        'sys_message': request.GET.get('message')
    })

def base_location(request, base_name):
    base = Base.objects.get(url=base_name)
    base.marker = 'images/markers/pointer_red.png'
    base.description = base.description.replace('"', '\"')
    base.description = re.sub('\s+', ' ', base.description)

    return render(request, 'bases/map.html', {
        'bases': [base],
        'single_base': True,
    })

def add_comment(request, base_id):
    base = get_object_or_404(Base, pk=base_id)

    if captcha.validate(request, RECAPTCHA_PRIVATE_KEY):
        comment = Comments(
            base_id=base_id,
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            band=request.POST.get('band', ''),
            content=request.POST.get('content', ''),
            rating=request.POST.get('rating', 0),
            date=datetime.datetime.now(),
            ip=request.META.get('REMOTE_ADDR')
        )
        comment.save()
        sys_message = 'Ваш комментарий добавлен'
    else:
        sys_message = 'Ошибка: Вы не прошли проверку Captcha'

    return HttpResponseRedirect('%s?message=%s' % (reverse('details', args=(base.url,)), sys_message))

def add_submit(request):
    return HttpResponseRedirect(reverse('add_done'))

def add_done(request):
    return render(request, 'bases/add_done.html', {})

def add(request):
    return render(request, 'bases/add.html', {
        'sys_message': request.GET.get('message')
    })

def contacts(request):
    return render(request, 'bases/contacts.html')
