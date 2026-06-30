from variaveis import gerar_nova_lista
from pesquisa_de_lista import pesquisa_lista


def sortear_lista(x, y, numero):
    tentativas = 0
    lista = gerar_nova_lista(x, y)
    while True:
        tentativas += 1
        indice = pesquisa_lista(lista, numero)
        if indice is not None:
            print(f'Número {numero} encontrado na posição {indice} da lista. Na tentativa {tentativas}')
            return indice, tentativas, lista
        

print(sortear_lista(20, 10 , 5))
