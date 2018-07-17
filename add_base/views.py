from captcha import captcha
from bases.models import Base, Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

def process_images(request):
    for file in request.FILES:
        print("Uploaded file: ")
        print(file.name)
    #print(request.FILES.get(0))

def add_submit(request):
    process_images(request)
    #return HttpResponseRedirect(reverse('add_done'))

def add_done(request):
    return render(request, 'bases/add_done.html', {})

def add(request):
    return render(request, 'bases/add.html', {
        'sys_message': request.GET.get('message')
    })
