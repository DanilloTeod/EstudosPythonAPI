from django.urls import path
from agenda.views import index, exibir_evento

urlpatterns = [
    path("", index), # path(caminho, para qual view deve apontar (funcao))
    path("evento", exibir_evento),
]