from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('settings/',views.settings,name='settings'),
    path('password/',views.password,name='password'),
    
    
]