from django.contrib import admin
from django.urls import path, include
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.result, name='result'),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('index_deep/', views.index_deep, name='deep'),    
]