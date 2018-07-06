from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Base

def map(request):
    bases_list = Base.get_all(request)
    return render(request, 'bases/map.html', {'bases': bases_list})

def list(request):
    bases_list = Base.get_all(request)
    return render(request, 'bases/list.html', {'bases': bases_list})

def details(request, base_name):
    return render(request, 'bases/details.html', {})

def add(request):
    return render(request, 'bases/add.html', {})
