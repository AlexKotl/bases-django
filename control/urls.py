from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    path('remind', views.remind, name='remind'),
    path('logout', views.logout, name='logout'),
]
