from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Destino, Alojamiento, Museo
from AppCoder.forms import DestinoForm, BusquedaDestinoForm
from django.contrib.auth.decorators import login_required

# Create your views here.def


def home(request):
    return render(request, "AppCoder/home.html")

def lista_destinos(request):
    destinos = Destino.objects.all()
    context={"destinos": destinos, "form_buscar": BusquedaDestinoForm()}
    return render(request, "AppCoder/destinos.html", context=context)



def detalle_destino(request, destino_id):
    destino=Destino.objects.get(id=destino_id)
    context={"destino": destino}
    return render(request, "AppCoder/detalle_destino.html", context=context)





@login_required
def crear_destino(request):
    if request.method=="POST":
        mi_formulario=DestinoForm(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data
            destino_save=Destino(titulo=informacion['titulo'], descripcion=informacion['descripcion'])
            destino_save.save()
            return redirect("AppCoderDestinos")
    context={"form": DestinoForm()}
    return render(request, 'AppCoder/crear_destino.html', context=context)

@login_required
def editar_destino(request, titulo):
    get_destino=Destino.objects.get(titulo=titulo)
    if request.method=="POST":
        mi_formulario=DestinoForm(request.POST)
        if mi_formulario.is_valid():
            informacion=mi_formulario.cleaned_data

            get_destino.titulo=informacion['titulo'] 
            get_destino.descripcion=informacion['descripcion']

            get_destino.save()
            return redirect("AppCoderDestinos")
    
    context={"titulo": titulo, "form": DestinoForm(initial={"titulo": get_destino.titulo , "descripcion": get_destino.descripcion})}
    return render(request, 'AppCoder/editar_destino.html', context=context)


@login_required
def eliminar_destino(request, titulo):
    get_destino=Destino.objects.get(titulo=titulo)
    get_destino.delete()
    return redirect("AppCoderDestinos")


def buscar_destino(request):
    mi_formulario=BusquedaDestinoForm(request.GET)
    if mi_formulario.is_valid():
        informacion=mi_formulario.cleaned_data
        destinos_filtrados=Destino.objects.filter(titulo__icontains=informacion['titulo'])
        context={"destinos": destinos_filtrados}
    
    return render(request, "AppCoder/buscar_destino.html", context=context)




def lista_alojamientos(request):
    alojamientos = Alojamiento.objects.all()
    return render(request, "AppCoder/alojamientos.html", {'alojamientos': alojamientos})

@login_required
def crear_alojamiento(request, titulo):
    save_alojamiento=Alojamiento(titulo=titulo)
    save_alojamiento.save()
    context={"titulo": titulo}
    return render(request, 'AppCoder/save_alojamiento.html', context)




def museos(request):
    return render(request, "AppCoder/museos.html")

def lista_museos(request):
    museos = Museo.objects.all()
    return render(request, "AppCoder/museos.html", {'museos': museos})

@login_required
def crear_museo(request, titulo):
    save_museo=Museo(titulo=titulo)
    save_museo.save()
    context={"titulo": titulo}
    return render(request, 'AppCoder/save_museo.html', context)