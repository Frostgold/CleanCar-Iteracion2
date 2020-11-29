from CleanCar.models import Insumo, Contacto
from rest_framework import serializers

# modelo a serializar

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["name", "precio", "descripcion", "stock"]

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ["name", "lastname", "asunto", "contacto", "mensaje"]
