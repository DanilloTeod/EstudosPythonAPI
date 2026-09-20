from django.db import models

class Categoria(models.Model): # mapea os atributos dessa classe para o db
    nome = models.CharField(max_length=256, unique=True)

    def __str__(self): # metodo chamado ao tentar imprimir um obj dessa categoria
        return f"{self.nome} <{self.id}>" # id vem da classe model

# Create your models here.
# classes que representam os modelos ou entidades da nossa aplicacao ex: usuarios
class Evento(models.Model):
    #cria os elementos no db
    nome = models.CharField(max_length=256) # não precisa ser unico, podemos ter dois eventos com mesmo nome sendo criado
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True) # é uma chave estrangeira para outro modelo
                                                                                   # caso seja deletado, setado como nulo
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True) # blank quer dizer que o campo pode ficar em branco

    # def __init__(self, nome, categoria, local=None, link=None):
    #     self.nome = nome
    #     self.categoria = categoria
    #     self.local = local
    #     self.link = link

    def __str__(self):
        return f"{self.nome} <{self.id}>" 
        
# aula_python = Evento("Aula de python", "backend", "Espirito santo")
# aula_js = Evento("Aula de JavaScript", "Fullstack", link="https://auladejs.com.br/")

# eventos = [
#     aula_js,
#     aula_python,
# ]
