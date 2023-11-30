from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro_home, name='pro_home')
]