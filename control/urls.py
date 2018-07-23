from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('login', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    #path('/submit', views.add_submit, name='add_submit'),
]
