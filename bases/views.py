from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def map(request):
    return render(request, 'bases/map.html', {})

def list(request):
    return render(request, 'bases/list.html', {})

def details(request, base_name):
    return render(request, 'bases/details.html', {})

def add(request):
    return render(request, 'bases/add.html', {})
