from No import No

class Lista_encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

# FUNÇÕES PARA ADICIONAR
    def append(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = no
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = no
        self.tamanho += 1

    def insert(self, index, valor):
        if index <= 0:
            no = No(valor)
            no.proximo = self.inicio
            self.inicio = no
            self.tamanho += 1
        elif index >= self.tamanho:
            self.append(valor)
        else:
            aux = self.inicio
            for i in range(index - 1):
                aux = aux.proximo
            no = No(valor)
            no.proximo = aux.proximo
            aux.proximo = no
            self.tamanho += 1

# FUNÇÕES PARA REMOVER
    def pop(self):
        if self.tamanho > 0:
            aux = self.inicio
            for i in range(self.tamanho - 2):
                aux = aux.proximo
            aux.proximo = None
            self.tamanho -= 1
        else:
            print("Não é possível remover um elemento de uma lista vazia")

    def remove(self, valor):
        aux = self.inicio
        if self.tamanho == 0:
            print("Não é possível remover de uma lista vazia")
        else:
            if aux.valor == valor:
                self.inicio = aux.proximo
                self.tamanho -= 1
            else:
                while aux.proximo is not None:
                    if aux.proximo.valor == valor:
                        aux.proximo = aux.proximo.proximo
                        self.tamanho -= 1
                        return
                    else:
                        aux = aux.proximo
                return print("Elemento não encontrado na lista")

# FUNÇÕES PARA EXIBIR A LISTA
    def mostrar(self):
        if self.tamanho > 0:
            aux = self.inicio
            while aux is not None:
                print(aux.valor, end=" ")
                aux = aux.proximo
            print()
        else:
            print("Lista vazia")

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.tamanho > 0:
            r = ""
            aux = self.inicio
            while aux:
                if aux.proximo != None:
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
