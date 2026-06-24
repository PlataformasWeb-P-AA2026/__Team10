from django.forms import ModelForm
from ordenamiento.models import Parroquia, BarrioCiudadela, PresidenteBarrio

# creacion de los formularios
class ParroquiaForm(ModelForm):
    class Meta:
        model = Parroquia
        fields = ['nombre', 'ubicacion', 'tipo']


class BarrioCiudadelaForm(ModelForm):
    class Meta:
        model = BarrioCiudadela
        fields = ['nombre', 'numero_viviendas', 'numero_parques', \
            'numero_edificios_residenciales', 'parroquia']


class PresidenteBarrioForm(ModelForm):
    class Meta:
        model = PresidenteBarrio
        fields = ['cedula', 'nickname', 'edad', 'profesion', 'barrio']
        
        

