from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('list', views.list, name='list'),
    path('contacts', views.contacts, name='contacts'),
    path('add', include('add_base.urls')),
    path('<str:base_name>', views.details, name='details'),
    path('<str:base_name>/location', views.base_location, name='base_location'),
    path('<str:base_id>/add_comment', views.add_comment, name='add_comment'),

]
