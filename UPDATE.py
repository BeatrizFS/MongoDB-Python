#Atualiza algum atributo de determinado produto.
from mongoengine.errors import DoesNotExist
from Arquivo1 import Produto

try:
    produto = Produto.objects(Nome="Arroz")
    produto.update(Valor=6.0)
    print("Produto atualizado!")
except DoesNotExist:
    print("Produto não encontrado")
