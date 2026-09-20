from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Olá mundo!")

def exibir_evento(request):
    evento = {
        "nome": "Aula teste",
        "categoria": "categoria teste",
        "local": "ES",
    }
    #template = loader.get_template("agenda/exibir_evento.html")
    #rendered_template = template.render(context={"evento": evento}, request=request) # injetar o contexto
    #return HttpResponse(rendered_template)
    return render(request=request, context={"evento": evento}, template_name="agenda/exibir_evento.html")



