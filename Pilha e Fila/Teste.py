# COMENTAR O TESTE QUE NÃO SERÁ USADO

from Pilha import *

pilha = Pilha()

# ADICIONANDO ELEMENTOS
pilha.inserir("A")
pilha.inserir("B")
pilha.inserir("C")
pilha.inserir("carro")

# REALIZANDO OS TESTES
pilha.remover()

print('-=' * 4)
print(pilha)
print('-=' * 4)

print(f'topo: {pilha.observar_pilha()}')
print(f'tamanho: {len(pilha)}')

# --------------------------------------------------- #

from Fila import *

fila = Fila()

# ADICIONANDO ELEMENTOS
fila.inserir("A")
fila.inserir("B")
fila.inserir("C")

# REALIZANDO OS TESTES
fila.remover()

print('-=' * len(fila))
print(fila)
print('-=' * len(fila))

print(fila.observar_fila())
print(f'tamanho: {len(fila)}')