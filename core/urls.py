from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('listado_filtro/<int:tipo_persona>/', views.ListadoPersonasFiltroTipoPersona, name='listado_filtro_cargo'),
    path('ingreso_personas/', views.IngresoPersonas, name='ingreso_personas'),
    path('listado_personas/', views.ListadoPersonas, name='listado_personas'),
    path('eliminar_persona/<id>/', views.Eliminar_Personas, name='eliminar_persona'),
    path('modificar_persona/<id>/', views.ModificacionPersonas, name='modificar_persona'),
    path('lista_filtro_cargo/<id>/', views.ListadoPersonasFiltroTipoPersona, name='lista_filtro_cargo'),
    path('lista_eventos/', views.ListadoEventos, name='lista_eventos'),
    path('lista_eventos_filtro_tipo/te/<int:tipo_evento>/', views.ListadoEventosFiltroTipoEvento, name='lista_eventos_filtro_tipo'),
    path('lista_eventos_filtro_comunidad/c/<int:comunidad>/', views.ListadoEventosFiltroComunidad, name='lista_eventos_filtro_comunidad'),
    path('administracion_comunidades/', views.AdministracionComunidades, name='administracion_comunidades'),
    path('listado_agentes_pastorales/', views.ListadoAgentesPastorales, name='listado_agentes_pastorales'),
    path('listado_comunidades', views.ListaComunidades, name='listado_comunidades')

]