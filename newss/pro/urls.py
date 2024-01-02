from django.urls import path
from . import views

urlpatterns = [
    path('', views.pro_home, name='pro_home'),
    path('pro_create', views.pro_create, name='pro_create'),
    path('<int:pk>', views.ProDetailView.as_view(), name='pro-detail'),
    path('<int:pk>/update', views.ProUpdateView.as_view(), name='pro-update'),
    path('<int:pk>/delete', views.ProDeleteView.as_view(), name='pro-delete')
    ]

