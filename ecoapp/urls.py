from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Reciclaje
    path('reciclaje/', views.lista_reciclaje, name='lista_reciclaje'),
    path('reciclaje/nuevo/', views.crear_reciclaje, name='crear_reciclaje'),
    path('reciclaje/editar/<int:pk>/', views.editar_reciclaje, name='editar_reciclaje'),
    path('reciclaje/eliminar/<int:pk>/', views.eliminar_reciclaje, name='eliminar_reciclaje'),
    # Plantacion
    path('plantacion/', views.lista_plantacion, name='lista_plantacion'),
    path('plantacion/nuevo/', views.crear_plantacion, name='crear_plantacion'),
    path('plantacion/editar/<int:pk>/', views.editar_plantacion, name='editar_plantacion'),
    path('plantacion/eliminar/<int:pk>/', views.eliminar_plantacion, name='eliminar_plantacion'),
]