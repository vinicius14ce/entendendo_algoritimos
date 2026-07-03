
import logging as log
import random
from typing import List


log.basicConfig(level=log.DEBUG)
log = log.getLogger(__name__)


class gerador:
    @staticmethod
    def get_list(x,y: int, ordenado: bool = False) -> List[int]:
        list = random.sample(range(x),y)
        return sorted(list) if ordenado else list
    
    def get_list2(x,y: int, ordenado: bool = False) -> List[int]:
        list = random.sample(range(x),y)
        list = sorted(list) if ordenado else list
        return list 

    def logger(random_list):
        log.debug(f"Random List: {random_list}")
        return log.debug()
    

    
    
x = 20
y = 10


#obj_logger = gerador.logger(gerador.sorted_list(x,y))
#print(f'print {gerador.logger(obj_logger)}/n','f{gerador.sorted_list(x,y)}' )
if __name__ == "__main__":
    print(gerador.get_list(x,y,ordenado=True))
    print(gerador.get_list(x,y,ordenado=False))

    print(gerador.get_list2(x,y,ordenado=True))
    print(gerador.get_list2(x,y,ordenado=False))

resultado = gerador.get_list(x, y, ordenado=True)

log.debug(f"Lista gerada: {resultado}")
print(resultado)