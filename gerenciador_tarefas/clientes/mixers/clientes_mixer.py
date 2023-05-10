from mixer.backend.django import mixer
from clientes.models import *
mixer.cycle(30).blend(Pedidos)