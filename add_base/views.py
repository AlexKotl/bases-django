from captcha import captcha
from bases.models import Base, Comments
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import AddForm

def process_images(request):
    for file in request.FILES:
        print("Uploaded file: ")
        print(file.name)
    #print(request.FILES.get(0))

def add_submit(request):
    #process_images(request)
    form = AddForm(request.POST)
    if form.is_valid():
        base = Base()
        base.address = form.cleaned_data['address']
        base.contacts = form.cleaned_data['contacts']
        base.pos_x = request.POST['pos_x']
        base.pos_y = request.POST['pos_y']
        base.name = form.cleaned_data['name']
        base.price = form.cleaned_data['price']
        base.description = form.cleaned_data['description']
        base.email = form.cleaned_data['email']
        base.password = form.cleaned_data['password']
        base.save()

        return HttpResponseRedirect(reverse('add_done'))
    else:
        return render(request, 'bases/add.html', {
            'form': AddForm(),
        })

def add_done(request):
    return render(request, 'bases/add_done.html', {})

def add(request):
    return render(request, 'bases/add.html', {
        'sys_message': request.GET.get('message'),
        'form': AddForm(),
    })
