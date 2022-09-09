from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('validate',views.validate,name='validate'),
    path('home/',views.home,name='home'),
    path('logout',views.leavepage,name='logout'),
]