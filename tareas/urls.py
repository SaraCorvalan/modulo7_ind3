
from django.contrib import admin
from django.urls import path
from tareas.views import tareas
from tareas.views import *
from django.contrib.auth import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', tareas, name = 'index'),
    path('registro_tareas/login/', tareas, name = 'index'),
    path('administra_tareas/login/', tareas, name = 'index'),
    
    path('registro_tareas/', formularioRegistroTareas, name = 'registro_tareas'),
    path('administra_tareas/', administraTareas, name = 'administra_tareas'),
   
    path('modifica_tareas/<id>/', modificaTareas, name="modifica_tareas"),
    path('elimina_tareas/<id>/', eliminaTareas, name = 'elimina_tareas'),
    path('completa_tareas/<id>/', completaTareas, name = 'completa_tareas'),
    path('login/', user_login, name = 'login'),
    path('login/', views.LoginView.as_view(template_name = 'registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name = 'registration/logout.html'), name='logout'),
    path('registro/', registro, name='registro'),
]

