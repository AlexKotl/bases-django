from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
    path('add/submit', views.add_submit, name='add_submit'),
    path('add/done', views.add_done, name='add_done'),
    path('contacts', views.contacts, name='contacts'),
    path('<str:base_name>', views.details, name='details'),
    path('<str:base_name>/location', views.base_location, name='base_location'),
    path('<str:base_id>/add_comment', views.add_comment, name='add_comment'),
]
