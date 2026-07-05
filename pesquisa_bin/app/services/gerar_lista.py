#classe criada para gerar uma lista de números aleatórios, com a opção de ordená-la.

import logging as log
import random
from typing import List


log.basicConfig(level=log.DEBUG)
log = log.getLogger(__name__)


class gerador:
    @staticmethod
    def get_list(x,y: int, order: bool = False):
        list = random.sample(range(x),y)
        return sorted(list) if order else list
    @staticmethod
    def get_list2(x,y: int, order: bool = False) -> List[int]:
        list = random.sample(range(x),y)
        list = sorted(list) if order else list
        return list 
    @staticmethod
    def logger(x,y: int) -> List[int]:
        return log.debug(gerador.get_list(x,y,order=False))
        
''' 

 

if __name__ == "__main__":

    x, y = 20, 10
    
    lista = gerador() 
    resultado = lista.get_list(x,y,order=True)
    print(resultado)
    print(gerador.get_list(x,y,order=False))

    print(gerador.get_list2(x,y,order=True))
    print(gerador.get_list2(x,y,order=False))

    resultado = gerador.get_list(x, y, order=True)

    log.debug(f"Lista gerada: {resultado}")
    print(resultado)

    #print(gerador.logger(20,10))
'''
