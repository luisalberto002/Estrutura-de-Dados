from No import No

class Lista_circular:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

# FUNÇÕES PARA ADICIONAR
    def append(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = self.fim = no
            self.inicio.proximo = self.fim
            self.fim.proximo = self.inicio
        else:
            aux = self.inicio
            while aux != self.fim:
                aux = aux.proximo
            aux.proximo = self.fim = no
            no.proximo = self.inicio
        self.tamanho += 1
    
    def insert(self, index, valor):
        aux = self.inicio
        no = No(valor)
        if index <= 0:
            no.proximo = aux
            self.inicio = no
            self.fim.proximo = no
        elif index >= self.tamanho:
            self.fim.proximo = no
            self.fim = no
            no.proximo = self.inicio
        else:
            for i in range(index - 1):
                aux = aux.proximo
            no.proximo = aux.proximo
            aux.proximo = no
        self.tamanho += 1

# FUNÇÕES PARA REMOVER
    def pop(self):
        if self.tamanho == 1:
            self.inicio = self.fim = None
        elif self.tamanho == 0:
            print("Não é possível remover de uma lista vazia")
            return
        else:
            aux = self.inicio
            while aux.proximo != self.fim:
                aux = aux.proximo
            self.fim = aux
            aux.proximo = self.inicio
        self.tamanho -= 1

    def remove(self, valor):
        aux = self.inicio
        if self.tamanho == 0:
            print("Não é possível remover de uma lista vazia")
        else:
            if aux.valor == valor:
                self.inicio = aux.proximo
                self.fim.proximo = self.inicio
                self.tamanho -= 1
            else:
                while aux.proximo != self.inicio:
                    if aux.proximo.valor == valor:
                        if aux.proximo == self.fim:
                            self.fim = aux
                            self.fim.proximo = self.inicio
                            self.tamanho -= 1
                            return
                        else:
                            aux.proximo = aux.proximo.proximo
                            self.tamanho -= 1
                            return
                    aux = aux.proximo
                return print("Elemento não encontrado na lista")

# FUNÇÕES PARA EXIBIR A LISTA
    def mostrar(self):
        if self.tamanho > 0:
            aux = self.inicio
            while aux:
                if aux.proximo != self.inicio:
                    print(aux.valor, end=" ")
                    aux = aux.proximo
                else:
                    print(aux.valor)
                    break
        else:
            print("Lista vazia")
    
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.tamanho > 0:
            r = ""
            aux = self.inicio
            while aux:
                if aux.proximo != self.inicio:
                    r += str(aux.valor) + " "
                    aux = aux.proximo
                else:
                    r += str(aux.valor)
                    break
            return r
        else:
            return "lista vazia"

# FUNÇÃO DE BUSCA DE ELEMENTO PELO INDICE
    def __getitem__(self, index):
        aux = self.inicio
        if index < 0 or index >= self.tamanho:
            return "list index out of range"
        else:
            for i in range(index):
                aux = aux.proximo
            return aux.valor
