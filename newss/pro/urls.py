from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro_home, name='pro_home'),
    path('pro_create', views.pro_create, name='pro_create')
]
