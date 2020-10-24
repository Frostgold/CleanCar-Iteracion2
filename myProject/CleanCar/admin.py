from django.contrib import admin
from .models import Instalacion, Empleado, Insumo, Slider, Vision

class InstalacionAdmin(admin.ModelAdmin):
    list_display = ['cod', 'name', 'direccion', 'imagen']
    search_fields = ['cod', 'name']
    list_per_page = 10

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['cod', 'name', 'descripcion', 'imagen']
    search_fields = ['cod', 'name']
    list_per_page = 10

class InsumoAdmin(admin.ModelAdmin):
    list_display = ['name', 'precio', 'stock', 'descripcion']
    search_fields = ['name']
    list_per_page = 10

class SliderAdmin(admin.ModelAdmin):
    list_display = ['cod', 'imagen']
    search_fields = ['cod']
    list_per_page = 10

class VisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'descripcion']
    search_fields = ['name']

# Register your models here.
admin.site.register(Instalacion, InstalacionAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Vision, VisionAdmin)
