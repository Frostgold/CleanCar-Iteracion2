from CleanCar.models import Insumo
from rest_framework import serializers

# modelo a serializar

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        flieds = ["nombre", "precio", "descripcion", "stock"]
