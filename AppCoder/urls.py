
from django.urls import path
from AppCoder.views import home, lista_destinos, detalle_destino, crear_destino, editar_destino, eliminar_destino, buscar_destino, lista_alojamientos, crear_alojamiento, lista_museos, crear_museo

urlpatterns = [
    path('home/', home, name="AppCoderHome"),

    path('destinos/', lista_destinos, name="AppCoderDestinos"),

    path('detalle_destino/<int:destino_id>/', detalle_destino, name="AppCoderDetalle_destino"),
    

    path('destino/crear', crear_destino, name='AppCoderCrearDestino'),
    path('destino/editar/<titulo>', editar_destino, name='AppCoderEditarDestino'),
    path('destino/eliminar/<titulo>', eliminar_destino, name='AppCoderEliminarDestino'),
    path('buscar_destino/', buscar_destino, name="AppCoderBuscarDestino"),

    path('alojamientos/', lista_alojamientos, name="AppCoderAlojamientos"),
    path('alojamiento/<titulo>', crear_alojamiento),

    path('museos/', lista_museos, name="AppCoderMuseos"),
    path('museo/<titulo>', crear_museo),

]
