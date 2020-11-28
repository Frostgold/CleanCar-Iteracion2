from django.shortcuts import render, redirect
from .models import Instalacion, Empleado, Insumo, Vision, Slider
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
import requests

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect(index)

def login(request):
    vision = Vision.objects.first()
    if request.POST:
        user = request.POST.get("usuario")
        password = request.POST.get("contrasena")
        us = authenticate(request, username=user, password=password)
        if us is not None and us.is_active:
           login_auth(request, us)
           return redirect(index)
        else:
            messages.info(request, 'usuario/contraseña inválidos')
            return redirect(login)

    return render(request, 'web/login.html', {'vision':vision})

def index(request):
    vision = Vision.objects.first()
    sliderFirst = Slider.objects.first()
    sliderLast  = Slider.objects.last()
    slider = Slider.objects.all()
    return render(request, 'web/index.html', {'slider':slider, 'first':sliderFirst, 'last':sliderLast, 'vision':vision})

def galeria(request):
    vision = Vision.objects.first()
    inst = Instalacion.objects.all()
    emp  = Empleado.objects.all()
    return render(request, 'web/galeria.html', {'lista_instalaciones':inst, 'lista_empleados':emp, 'vision':vision})

def ubicaciones(request):
    vision = Vision.objects.first()
    return render(request, 'web/about.html', {'vision':vision})

def formulario(request):
    vision = Vision.objects.first()
    if request.POST:
        nombre      = request.POST.get("nombre")
        apellido    = request.POST.get("apellido")
        correo      = request.POST.get("correo")
        usuario     = request.POST.get("usuario")
        contrasena  = request.POST.get("contrasena")

        try:
            u = User.objects.get(username=usuario)
            messages.info(request, 'El usuario ya existe')
            return redirect(formulario)
        except:
            u = User()
            u.first_name = nombre
            u.last_name  = apellido
            u.username   = usuario
            u.email      = correo
            u.set_password(contrasena)
            u.save()

            us = authenticate(request, username=usuario, password=contrasena)
            login_auth(request, us)
            return redirect(index)

    return render(request, 'personal/formulario.html', {'vision':vision})

@login_required(login_url='/login')
@permission_required('CleanCar.add_insumo', login_url='/login/')
def admin_insumos(request):
    vision = Vision.objects.first()
    response = requests.get("http://127.0.0.1:8000/api/insumos/")
    insumo = response.json()
    if request.POST:
        accion = request.POST.get("accion")

        if accion == "registrar":
            nombre      = request.POST.get("nombre")
            precio      = request.POST.get("precio")
            stock       = request.POST.get("stock")
            descripcion = request.POST.get("descripcion")

            datos_api = {
                "name": nombre,
                "precio": precio,
                "descripcion": descripcion,
                "stock": stock
            }
            respuesta = requests.post("http://127.0.0.1:8000/api/insumos/", data=datos_api)
            messages.success(request, 'Se agregó un insumo')

            return redirect(admin_insumos)

    return render(request, 'personal/adm_insumos.html', {'lista_insumos':insumo, 'vision':vision})

@login_required(login_url='/login')
@permission_required('CleanCar.delete_insumo', login_url='/login/')
def eliminar_insumo(request, id):
    try:
        eliminar_insumo = Insumo.objects.get(name=id)
        eliminar_insumo.delete()
        messages.success(request, 'Se eliminó un insumo')
    except:
        messages.info(request, 'No se eliminó insumo')

    return redirect(admin_insumos)

@login_required(login_url='/login')
@permission_required('CleanCar.change_insumo', login_url='/login/')
def modificar_insumo(request, id):
    vision = Vision.objects.first()
    try:
        modificar_insumo = Insumo.objects.get(name=id)
        return render(request, 'personal/modificar_insumo.html', {'item':modificar_insumo, 'vision':vision})
    except:
        return redirect(admin_insumos)

@login_required(login_url='/login')
@permission_required('CleanCar.change_insumo', login_url='/login/')
def actualizar(request):
    if request.POST:
        nombre      = request.POST.get("nombre")
        precio      = request.POST.get("precio")
        stock       = request.POST.get("stock")
        descripcion = request.POST.get("descripcion")

        try:
            insumos = Insumo.objects.get(name=nombre)
            insumos.precio      = precio
            insumos.stock       = stock
            insumos.descripcion = descripcion

            insumos.save()
            messages.success(request, 'Insumo actualizado')
        except:
            messages.info(request, 'No se modificó insumo')

        return redirect(admin_insumos)
