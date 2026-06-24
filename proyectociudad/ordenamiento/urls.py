from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parroquias/', views.listar_parroquias, name='listar_parroquias'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear-parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('editar-parroquia/<int:id>/', views.editar_parroquia, name='editar_parroquia'),
    path('crear-barrio/', views.crear_barrio, name='crear_barrio'),
    path('editar-barrio/<int:id>/', views.editar_barrio, name='editar_barrio'),
]


