from Lista_encadeada import *

lista = Lista_encadeada()

# ADICIONANDO ELEMENTOS
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

# REALIZACAO DOS TESTES
print("ANTES:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')

print(lista[3])

print("\nDEPOIS:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')
