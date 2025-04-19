#=============== EX 1 Como buscar um valor em uma lista encadeada======================================#
# Conceito: Percorremos a lista do início até o fim comparando com o valor procurado.
# Enunciado: Faça um teste buscando os valores 20 e 50.
#========================================================================================================

def buscar(inicio, valor):
    atual=inicio
    while atual:
        if atual["valor"]==valor:
            return True
        atual=atual["próximo"]
    return False

lista= {
    "valor":5,
    "próximo":{
        "valor":8,
        "próximo":{
            "valor":12,
            "próximo":None
        }
    }
}

print(buscar(lista,50))

#==================== 2 * //Como inserir um valor no final da lista encadeada*  ======================#
# Conceito: Andamos até o último nó (que aponta para None) e colocamos um novo nó lá
# Enunciado: Adicione o valor 40 ao final de uma lista que já tem 10 → 20 → 30.
#========================================================================================================
def inserir(inicio, valor):
    atual = inicio
    while atual:
        if atual["proximo"] is None:
            atual["proximo"] = {
                "valor": valor,
                 "proximo" : None
                 }
            break
        atual = atual["proximo"]


lista2 = {
    "valor": 10,
    "proximo": {
        "valor" : 20,
        "proximo" :{
            "valor" : 30,
            "proximo" : None
        }
    }}

print(inserir(lista2, 40))

#======================= 3 - Como remover um valor da lista encadeada ==============================================
# Conceito: Se for o primeiro valor, atualizamos o início. Se for no meio ou fim, fazemos
# o nó anterior apontar para o próximo.
# Enunciado: Remova o valor 20 da lista 10 → 20 → 30.
#========================================================================================================

def remover(inicio, valor):

    atual = inicio

    if atual["valor"] == valor:
        atual = atual["proximo"]
    else:
            while atual:
                if atual["valor"] == valor:
                    atual = atual["proximo"]["proximo"]
                    break
                atual = atual["proximo"]


lista3 = {
    "valor": 10,
    "proximo": {
        "valor" : 20,
        "proximo" :{
            "valor" : 30,
            "proximo" : None
        }
    }} 

print(remover(lista3, 20))
lista3

#============#alterando pelo Github e fazendo upload no vsCode =================#

#Criando listas encadeadas na mão:
list1 = {
    "valor" : 1,
    "proximo" : {
        "valor" : 2,
        "proximo" : {
            "valor" : 4,
            "proximo" : None


        }
    }
}


list2 = {
    "valor" : 3,
    "proximo" : {
        "valor" : 5,
        "proximo" : {
            "valor" : 1,
            "proximo" : None
        }
    }
}
