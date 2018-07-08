from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.map, name='map'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('contacts/', views.map, name='contacts'),
    path('<str:base_name>', views.details, name='details'),
    path('<str:base_id>/add_comment', views.add_comment, name='add_comment'),
]
