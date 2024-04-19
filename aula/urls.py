from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.home),
    path('añadir_pag/', views.añadir_pag),
    path('añadir_est/', views.añadir_est ),
    path('listado/eliminar/<cedula>', views.eliminar),
    path('listado/', views.listado),
    path('listado/editar_pag/<cedula>', views.editar_pag),
    path('editar_est/', views.editar_est),
    
]