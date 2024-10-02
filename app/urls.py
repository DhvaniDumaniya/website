from turtle import home
from django.urls import path # type: ignore
# from django.contrib.auth import views as auth_views
from app import views
from app.views import *

urlpatterns = [
   path('sign',sign,name="sign"),
   path('register',register,name='register'),
   path('',login,name='login'),
   path('home1',home1,name='home1'),
   path('home',home,name="home"),
   # path('login', auth_views.LoginView.as_view(), name='login'), 
   path('contact',contact,name="contact"), 
   path('aboutus',aboutus,name="aboutus"),
   # path('name',users_list,name=users_list),
]

# urlpatterns = [
#     path('', views.home, name='home'), 
     
#     path('about', aboutus, name='aboutus'),  
#     path('contact', contact, name='contact'), 
    
# ]
