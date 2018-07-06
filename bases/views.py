from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Base

def map(request):
    return render(request, 'bases/map.html', {
        'bases': Base.get_all(request),
        'bases_latest': Base.get_latest(request),
    })

def list(request):
    return render(request, 'bases/list.html', {
        'bases': Base.get_all(request),
    })

def details(request, base_name):
    return render(request, 'bases/details.html', {
        'base': Base.objects.get(url=base_name)
    })

def add(request):
    return render(request, 'bases/add.html', {})
