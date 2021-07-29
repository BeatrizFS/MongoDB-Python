#DELETE
from mongoengine.errors import DoesNotExist
from Arquivo1 import Produto

try:
    produto = Produto.objects(Nome="Tilápia").get()
    produto.delete()
    print("Produto deletado")
except DoesNotExist:
    print("Produto não encontrado")
