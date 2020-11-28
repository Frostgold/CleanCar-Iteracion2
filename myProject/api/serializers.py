from CleanCar.models import Insumo
from rest_framework import serializers

# modelo a serializar

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["name", "precio", "descripcion", "stock"]
