from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('auth', views.auth, name='auth'),
    path('remind', views.remind, name='remind'),
    path('logout', views.logout, name='logout'),
    path('edit/<base_id>', views.edit_base, name='edit_base'),
    path('save/<base_id>', views.save_base, name='save_base'),
    path('block/<base_id>', views.block_base, name='block_base'),
    path('unblock/<base_id>', views.unblock_base, name='unblock_base'),
]
