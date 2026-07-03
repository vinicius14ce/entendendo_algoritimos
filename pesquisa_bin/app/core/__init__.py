
import logging as log
from dataclasses import dataclass
import random

x = 20
y = 10

@dataclass  
class gerador:
    def sorted_list(x,y):
        return sorted(random.sample(range(x),y))
    
    def random_list(x,y):
        return random.sample(range(x),y)

    def print_rlist(random_list):
        print(random_list)

    def repr(random_list):
        return repr(f"Random List: {random_list}")
    
    def logger(random_list):
        log.basicConfig(level=log.DEBUG)
        log.debug(f"Random List: {random_list}")
        return log.debug()

print(gerador.sorted_list(x,y))

print(gerador.logger)
