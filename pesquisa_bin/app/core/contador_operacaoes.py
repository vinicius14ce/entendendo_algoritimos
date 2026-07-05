#Aqui vai ficar o contador de operações,
# que vai contar quantas operações foram feitas para encontrar o número na lista.
#Vou montar um decorator para contar as operações,
# e depois vou criar uma função que vai receber a lista
# e o número a ser pesquisado, e vai retornar o índice do número na lista, 
# ou None se não for encontrado.

from functools import wraps
import inspect


a, b = 5, 5

def test_wrapper(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@test_wrapper
def contador(a, b):
    return a + b, a, b

print(contador(a, b), contador.__name__)
print(contador.__code__)
