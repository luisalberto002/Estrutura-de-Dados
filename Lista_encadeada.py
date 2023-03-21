from No import No

class Lista_encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = no
            self.inicio.proximo = None
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = no
        self.tamanho += 1
            
    def mostrar (self):
        aux = self.inicio
        while aux is not None:
            print(aux.valor)
            aux = aux.proximo

lista = Lista_encadeada()
lista.inserir(23)
lista.inserir(42)
lista.mostrar()
print(f'tamanho: {lista.tamanho}')