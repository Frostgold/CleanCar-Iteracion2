from django.shortcuts import render

from CleanCar.models import Insumo, Contacto
from .serializers import InsumosSerializer, ContactoSerializer
from rest_framework import generics

# Create your views here.
class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumosSerializer

class InsumosFiltroNombreViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset(self):
        elnombre = self.kwargs['nombre']
        return Insumo.objects.filter(name=elnombre)
    
class InsumosFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset(self):
        elprecio = self.kwargs['precio']
        return Insumo.objects.filter(precio=elprecio)    

class ContactoViewSet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
