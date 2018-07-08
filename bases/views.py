import re
import urllib
import datetime
from .models import Base, Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        'sys_message': request.GET['message']
    })

def add_comment(request, base_id):
    base = get_object_or_404(Base, pk=base_id)
    comment = Comments(
        base_id=base_id,
        name=request.POST['name'],
        email=request.POST['email'],
        band=request.POST['band'],
        content=request.POST['content'],
        rating=request.POST['rating'],
        date=datetime.datetime.now(),
        ip=request.META.get('REMOTE_ADDR')
    )
    comment.save()

    return HttpResponseRedirect('%s?message=%s' % (reverse('details', args=(base.url,)), "Ваш комментарий добавлен"))

def add(request):
    return render(request, 'bases/add.html', {})

def contacts(request):
    return render(request, 'bases/contacts.html')
