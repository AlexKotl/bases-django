from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('/submit', views.add_submit, name='add_submit'),
    path('/done', views.add_done, name='add_done'),
]
