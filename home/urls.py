
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index , name = 'home'),
    path('userRegister', views.userRegister , name = 'userRegister'),
    path('userLogin', views.userLogin , name = 'userLogin'),
    path('userEdit', views.userEdit , name = 'userEdit'),
    path('userLogout', views.userLogin )
]