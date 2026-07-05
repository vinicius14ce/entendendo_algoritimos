#Aqui vai ficar o contador de operações,
# que vai contar quantas operações foram feitas para encontrar o número na lista.
#Vou montar um decorator para contar as operações,
# e depois vou criar uma função que vai receber a lista
# e o número a ser pesquisado, e vai retornar o índice do número na lista, 
# ou None se não for encontrado.

from functools import wraps

class decorator:
    def wrapper_contagem(self, func):
        @wraps(func)
        def wrapper(*args):
            contagem = len(func(*args))
            wrapper.contagem += 1
            return func(*args)
        wrapper.contagem = 0
        return wrapper
    
    '''
    def wrapper_contagem(func):
        @wraps(func)
        def wrapper(*args):
            contagem = len(func(*args))
            wrapper.contagem += 1
            return func(*args)
        wrapper.contagem = 0
        return wrapper
    '''

x, y = 1, 2
decorator = decorator()
wrapper = decorator.wrapper_contagem()

@wrapper
def args(x, y): 
    return(x + y)

print(args(x, y), args.__name__)





'''

a, b = 5, 5

def test_wrapper(func):
    @wraps(func)
    def wrapper(*args):
        x = 2 * func(*args) #f"Called {func.__name__} with arguments: {args}"
        return x
    return wrapper

    
@test_wrapper
def contador(a, b):
    return a + b, a, b

print(contador(a, b), contador.__name__)
print(contador.__code__)
print(test_wrapper(contador(a, b)))


#Testes de construção de decorators e wrappers, 
# inserir retornos em funções.
# e o decorator @wraps para manter metadados de funções que são decoradas.

'''