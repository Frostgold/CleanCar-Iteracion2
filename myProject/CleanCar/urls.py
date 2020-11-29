from django.contrib import admin
from django.urls import path, include
from .views import login, logout_view, index, galeria, formulario, ubicaciones, contacto, admin_insumos, eliminar_insumo, modificar_insumo, actualizar, guardar_token

urlpatterns = [
    path('', index, name='INDEX'),
    path('login/', login, name='LOGIN'),
    path('logout/', logout_view, name='LOGOUT'),
    path('galeria/', galeria, name='GALERIA'),
    path('formulario/', formulario, name='FORMULARIO'),
    path('ubicaciones/', ubicaciones, name='UBICACIONES'),
    path('contacto/', contacto, name='CONTACTO'),
    path('admin_insumos/', admin_insumos, name='ADM_INSUMOS'),
    path('eliminar_insumo/<id>/', eliminar_insumo, name="ELIMINAR"),
    path('modificar_insumo/<id>/', modificar_insumo, name="MODIFICAR"),
    path('actualizar/', actualizar, name="ACTUALIZAR"),
    path('accounts/login/', login, name="ACCOUNTSLOGIN"),

    path('oauth/', include('social_django.urls', namespace='social')),
    path('guardar-token/', guardar_token, name='guardar-token'),
]
