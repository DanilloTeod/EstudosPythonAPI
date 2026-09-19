from django.db import models

# Create your models here.
# classes que representam os modelos ou entidades da nossa aplicacao ex: usuarios

class Evento:
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link
        
aula_python = Evento("Aula de python", "backend", "Espirito santo")
aula_js = Evento("Aula de JavaScript", "Fullstack", link="https://auladejs.com.br/")

eventos = [
    aula_js,
    aula_python,
]
