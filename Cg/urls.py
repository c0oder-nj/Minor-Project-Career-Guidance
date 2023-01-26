from django.contrib import admin
from django.urls import path,include
from Cg import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('login',views.Userlogin,name="login"),
    path('register',views.register,name="register"),
    path('Test',views.Test,name="Test"),
    path('logout',views.Userlogout,name="logout"),
    path('10th',views.tenth,name='10th'),
    path('12th',views.twelth,name="12th"),
    path('Homeal',views.Homeal,name="Homeal")
]