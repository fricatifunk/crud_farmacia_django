from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('remedios',views.listadoRemedios),
    path('agregarRemedios',views.agregarRemedios),
    path('eliminar/<int:id>',views.eliminarRemedio,name='eliminar'),
    path('actualizarRemedio/<int:id>',views.actualizarRemedio,name='actualizar'),
    
]