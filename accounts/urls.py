from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import Register,Login,Logout

urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('register/',Register.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
    
]