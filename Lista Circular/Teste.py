from Lista_circular import *

lista = Lista_circular()

# ADICIONANDO ELEMENTOS
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

# REALIZACAO DOS TESTES
print("ANTES:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')

lista.remove(1)

print("\nDEPOIS:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')
