from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('',views.accounts, name='accounthome'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('dhome', views.dhome, name="dhome"),
    path('appointments/',views.appointments, name="appointments"),
    path('logout/',views.logout, name = "logout")
    
    
]