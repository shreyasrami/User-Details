from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('',Details.as_view(),name='details'),
    path('del/',Del.as_view(),name='del'),
    path('edit/',Edit.as_view(),name='edit'),
    
]