from django.urls import path
from . import views

app_name = 'mi_admin'

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'), 
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('editar_usuario/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('<int:pk>/usuario_actividad/', views.actividad_usuario, name='actividad_usuario'),
    path('lista_puertas/', views.lista_puertas, name='lista_puertas'),
    path('puerta_info/<int:pk>/', views.puerta_info, name='puerta_info'),
    path('editar_puerta/<int:pk>/', views.editar_puerta, name='editar_puerta'),
    path('eliminar_puerta/<int:pk>/', views.eliminar_puerta, name='eliminar_puerta'),
    path('nueva_puerta/', views.nueva_puerta, name='nueva_puerta'),
]
