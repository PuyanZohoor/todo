from django.urls import path

from . import views

urlpatterns = [
    path('index/add', views.add, name='todo.views.add'),
    path('index/<int:id>/edit', views.edit, name='todo.views.edit'),
    path('index/<int:id>/delete', views.delete, name='todo.views.delete'),
    path('index/', views.list, name='todo.views.list'),
]