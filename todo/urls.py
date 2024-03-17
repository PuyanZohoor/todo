from django.urls import path

from . import views

urlpatterns = [
    path('index', views.add, name='index'),
    path('index', views.edit, name='index'),
    path('index', views.delete, name='index'),
    path('index', views.list, name='index'),
]