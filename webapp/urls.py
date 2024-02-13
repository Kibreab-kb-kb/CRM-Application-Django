from django.urls import path
from . import views

urlpatterns = [ 

    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create_record',views.create_record,name='create_record'),
   

]
