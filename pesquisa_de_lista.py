'''Criação de uma função para pesquisar um número em uma lista de números aleatórios'''
import random
x = 10
y = 5
lista_random = list(random.sample(range(x),y))
''' sorted(lista_random) or lista_random.sort() '''
lista_seq = sorted(lista_random) 

def pesquisa_lista (lista, numero):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == numero:
            return meio
        if chute > numero:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None 

'''print(pesquisa_lista(lista_seq,5000)) 

print(lista_seq)'''

def sortear_lista(lista, numero):
    tentativas = 0
    while True:
        tentativas += 1
        indice = pesquisa_lista(lista, numero)
        if indice is not None:
            print(f'Número {numero} encontrado na posição {indice} da lista. Na tentativa {tentativas}')
            return indice, tentativas, lista
        

print(sortear_lista(lista_seq, 5))
    