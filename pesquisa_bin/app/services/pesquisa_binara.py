from typing import List

class PesquisaBinaria:
    def __init__(self, lista)-> List:
        self.lista = lista

    def pesquisa_lista (self, numero):
        a = 0
        o = len(self.lista) - 1
        while a <= o:
            meio = (a + o) // 2
            chute = self.lista[meio]
            if chute == numero:
                return meio
            if chute > numero:
                o = meio - 1
            else:
                a = meio + 1

        return None 


# condicional permite que o código seja executado apenas quando o arquivo é executado diretamente.
if __name__ == "__main__":

    pesquisa = PesquisaBinaria([1, 3, 35, 7, 90, 11, 13, 0, 17, 19])
    print(pesquisa.pesquisa_lista(3))
    print(pesquisa.lista)
#-------------------------------------------------------------------------------------------------.

