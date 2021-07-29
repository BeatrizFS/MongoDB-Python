from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import BooleanField, EmailField, FloatField,IntField, ReferenceField, StringField
from mongoengine import *
# Instituto Federal de Pernambuco - Campus Paulista
# Disciplina: Banco de Dados 2
# Professor: Flávio Oliveira
# Alunos: Weslley Ferreira Félix e Beatriz Silva
# ---------> Projeto de Fim de Disciplina - CRUD MongoDB e Python<-----------
#______________________________________________________________________________

connect("SuperMercadoBDPY")
class Produto(Document):
    Nome = StringField(required=True, max_length=50)
    Marca = StringField(required=True)
    Valor = FloatField(required=True)
    Quantidade = IntField(required=True)
    admin = BooleanField(default=False)
    registered = BooleanField(default=False)

produto = Produto(
    Nome="Feijão",
    Marca="Kicaldo",
    Valor=10.50,
    Quantidade=10,
)

produto.admin = True
produto.registered = True
produto.save()

produto = Produto(
    Nome="Arroz",
    Marca="Camil",
    Valor=5.0,
    Quantidade=10,
)
produto.admin = True
produto.registered = True
produto.save()

print("Produtos salvos")

class Cliente(Document):
    Nome = StringField(required=True)
    Endereço = StringField(required=True, unique=True)
    Email = EmailField(unique=True)
    CPF = StringField(unique=True)

class Mercado(Document):
    Estabelecimento = StringField(required=True)
    Endereço = StringField(required = True)
    Itens=ReferenceField(Produto)


Mercado(
    Estabelecimento = "Atacadão",
    Endereço = "Av.PE-15, 321 - Olinda/PE",
    Itens= produto,
).save()

print("Mecado salvo")

print("Concluído")