from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import Usuario, Actividad, Puerta
from datetime import datetime

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'rol', 'telefono', 'fecha_nacimiento']

class PuertaForm(ModelForm):
    class Meta:
        model = Puerta
        fields = ['nombre', 'ubicacion', 'estado', 'fecha_instalacion']

def pagina_principal(request):
    return render(request, 'mi_admin/pagina_principal.html')

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {'usuarios': usuarios}
    return render(request, 'mi_admin/lista_usuarios.html', contexto)

def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    mensaje = None

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            mensaje = 'Usuario actualizado correctamente'
            return redirect('mi_admin:lista_usuarios')  # Redireccionar a la lista de usuarios
    else:
        formulario = UsuarioForm(instance=usuario)
    
    contexto = {'formulario': formulario, 'mensaje': mensaje, 'usuario': usuario}
    return render(request, 'mi_admin/editar_usuario.html', contexto)

def eliminar_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    usuario.delete()
    return redirect('mi_admin:lista_usuarios')

def actividad_usuario(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    actividades = Actividad.objects.filter(usuario=usuario)
    contexto = {'usuario': usuario, 'actividades': actividades}
    return render(request, 'mi_admin/actividad_usuario.html', contexto)

def nuevo_usuario(request):
    mensaje = None

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje = 'Usuario guardado correctamente'
            formulario = UsuarioForm()  
        else:
            mensaje = 'Error al guardar el usuario. Por favor, verifica los datos ingresados.'
    else:
        formulario = UsuarioForm()
    
    contexto = {'formulario': formulario, 'mensaje': mensaje}
    return render(request, 'mi_admin/nuevo_usuario.html', contexto)

    
def lista_puertas(request):
    puertas = Puerta.objects.all()
    contexto = {'puertas': puertas}
    return render(request, 'mi_admin/lista_puertas.html', contexto)

def puerta_info(request, pk):
    puerta = Puerta.objects.get(pk=pk)
    actividades = Actividad.objects.filter(puerta=puerta)
    contexto = {'puerta': puerta, 'actividades': actividades}
    return render(request, 'mi_admin/puerta_info.html', contexto)


def editar_puerta(request, pk):
    puerta = get_object_or_404(Puerta, pk=pk)
    mensaje = None

    if request.method == 'POST':
        formulario = PuertaForm(request.POST, instance=puerta)
        if formulario.is_valid():
            formulario.save()
            mensaje = 'Puerta actualizada correctamente'
            return redirect('mi_admin:lista_puertas')
    else:
        formulario = PuertaForm(instance=puerta)
    
    contexto = {'formulario': formulario, 'mensaje': mensaje, 'puerta': puerta}
    return render(request, 'mi_admin/editar_puerta.html', contexto)

def eliminar_puerta(request, pk):
    puerta = Puerta.objects.get(pk=pk)
    puerta.delete()
    return redirect('mi_admin:lista_puertas')

def nueva_puerta(request):
    mensaje = None

    if request.method == 'POST':
        formulario = PuertaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            mensaje = 'Puerta guardada correctamente'
            formulario = PuertaForm()  
    else:
        formulario = PuertaForm()
    
    contexto = {'formulario': formulario, 'mensaje': mensaje}
    return render(request, 'mi_admin/nueva_puerta.html', contexto)