from Arquivo1 import Produto
#READ
#Consultar o Banco de dados
#1.Retorna todas as informações do Banco de dados
produtos = Produto.objects()

print(produtos)

for produto in produtos:
    print(produto.Nome, produto.Valor)