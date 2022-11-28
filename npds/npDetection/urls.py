from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('validate',views.validate,name='validate'),
    path('logout',views.leavepage,name='logout'),
    path('main-page/',views.mainpage,name='main-page'),
    path('admin-main/',views.adminmain,name='admin-main'),
    path('user-main/',views.usermain,name='user-main'),
    path('user-main-page/',views.usermainpage,name='user-main-page'),
    path('admin-profile',views.admin_profile,name='admin-profile'),
    path('change-password',views.change_password,name='change-password'),
    path('changepass/',views.passChange,name='passChange'),
    path('check-records',views.checkRecords,name='check-records'),
    path('add-authority',views.addAuthority,name='add-authority'),
    path('check-authority',views.checkAuthority,name='check-authority'),    
    path('add-user',views.addUser,name='add-user'),
    path('view-user',views.viewUser,name='view-user'),
    path('delete-user',views.deleteUser,name='delete-user'),
    path('add-user-db',views.addusertodb,name='add-user-db'),
    path('open-camera', views.camerarequest, name='open-camera'),

]