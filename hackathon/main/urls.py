from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('connect/',views.connect,name='connect'),
    path('login/',auth_view.LoginView.as_view(),name="login"),
    path('settings/',views.settings,name='settings'),
    path('password/',views.password,name='password'),

    # path('signup/',views.signup,name="signup"),
    path('signup/',views.selection,name="selection"),
    path('logout/',auth_view.LogoutView.as_view(),name="logout"),

    path('signup/client',views.client,name="client"),
    path('signup/psychologist',views.psychologist,name="psychologist"),
    
]