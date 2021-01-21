from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda req: redirect('landing')),
    path('app/landing/',views.landing,name='landing'),
    path('app/new/',views.new_user,name='new_user'),
    path('app/log_out',views.log_out,name='log_out'),
    path('app/log_in',views.log_in,name='log_in')
]