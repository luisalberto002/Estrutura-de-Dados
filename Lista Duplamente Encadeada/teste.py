from Lista_Duplamente_Ecadeada import *

lista = Lista_Duplamente_Encadeada()

# ADICIONANDO ELEMENTOS
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

# REALIZACAO DOS TESTES
print("ANTES:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')

lista.remove(2)
lista.append(9)
lista.insert(1, 7)

lista.ver_ponteiro()

print("DEPOIS:")
print(f'[{lista}]  tamanho:{lista.tamanho}\n')
