'''Criação de uma função para pesquisar um número em uma lista de números aleatórios'''
from variaveis import gerar_nova_lista
# importa do arquivo variaveis.py a função gerar_nova_lista
lista_seq = gerar_nova_lista(20, 10)


# função define valores base de baixo e alto, e enquanto baixo for menor ou igual a alto, 
# calcula o meio da lista e compara o valor do meio com o número procurado. 
# Se o valor do meio for igual ao número procurado, retorna o índice do meio. 
# Se o valor do meio for maior que o número procurado, ajusta o valor de alto para meio - 1. 
# Caso contrário, ajusta o valor de baixo para meio + 1. 
# Se o número não for encontrado, retorna None. 

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

print(pesquisa_lista(lista_seq,5)) 

print(lista_seq)

