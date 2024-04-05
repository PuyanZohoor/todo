from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('index/add', views.add, name='todo.views.add'),
    path('index/<int:id>/edit', views.edit, name='todo.views.edit'),
    path('index/<int:id>/delete', views.delete, name='todo.views.delete'),
    path('index/', views.list, name='todo.views.list'),
    path('login/', views.login_page, name='todo.views.login_page'),
    path('signup/', views.sign_up, name='todo.views.sign_up'),
    path('index/logout', views.logout_part, name='todo.views.logout_part'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)