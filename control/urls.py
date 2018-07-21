from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    #path('/submit', views.add_submit, name='add_submit'),
]
