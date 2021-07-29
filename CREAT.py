from mongoengine.errors import NotUniqueError
from Arquivo1 import Produto

#CREAT
#Cria novos produtos
produto = Produto(
    Nome = "Macarão",
    Marca = "Vitarella",
    Valor = 4.30,
    Quantidade = 30,
)

produto.admin = True
produto.registered = True
produto.save()

produto = Produto(
    Nome = "Tilápia",
    Marca = "Peixefundo",
    Valor = 35.6,
    Quantidade = 1,
)
produto.admin = True
produto.registered = True
produto.save()

#Avisa que o registro não é único
try:
    produto.save()
except NotUniqueError:
    print("Produto e valores não são únicos.")