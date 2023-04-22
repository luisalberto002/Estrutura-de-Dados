from No import No

class Lista_Duplamente_Encadeada:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

# FUNÇÕES DE ADICIONAR
    def append(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = no
        else:
            aux = self.inicio
            while aux.proximo is not None:
                aux = aux.proximo
            aux.proximo = no
            no.anterior = aux
        self.tamanho += 1

    def insert(self, index, valor):
        if index <= 0:
            no = No(valor)
            self.inicio.anterior = no
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
            aux.proximo.anterior = no
            no.proximo = aux.proximo
            no.anterior = aux
            aux.proximo = no
            self.tamanho += 1

# FUNÇÕES DE REMOVER
    def pop(self):
        if self.tamanho == 0:
            print("Não é possível remover de uma lista vazia")
        else:
            aux = self.inicio
            for i in range(self.tamanho - 2):
                aux = aux.proximo
            aux.proximo = None
            self.tamanho -= 1

# falta ajeitar
    def remove(self, valor):
        aux = self.inicio
        if self.tamanho == 0:
            print("Não é possível remover de uma lista vazia")
        else:
            if aux.valor == valor:
                self.inicio = aux.proximo
                aux.proximo.anterior = None
                self.tamanho -= 1
            else:
                while aux.proximo is not None:
                    if aux.proximo.valor == valor:
                        aux.proximo = aux.proximo.proximo
                        aux.proximo.anterior = aux
                        self.tamanho -= 1
                        return
                    else:
                        aux = aux.proximo
                return print("elemento não encontrado a lista")

# FUNÇÕES PARA EXIBIR

    def ver_ponteiro(self):
        if self.tamanho > 0:
            aux = self.inicio
            while aux is not None:
                if aux.anterior is None:
                    print("n", end=" <- ")
                else:
                    print(aux.anterior.valor, end=" <- ")
                print(aux.valor, end=" -> ")
                if aux.proximo is None:
                    print("n\n")
                else:
                    print(aux.proximo.valor)
                aux = aux.proximo
        else:
            print("Lista vazia")

    def mostrar_lista(self):
        if self.tamanho > 0:
            aux = self.inicio
            while aux is not None:
                print(aux.valor, end=" ")
                aux = aux.proximo
            print()
        else:
            print("Lista vazia")

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
            return "Lista vazia"

    def __str__(self):
        return self.__repr__()

# FUNÇÃO DE BUSCA DE ELEMENTO PELO INDICE
    def __getitem__(self, index):
        aux = self.inicio
        if index < 0 or index >= self.tamanho:
            return "list index out of range"
        else:
            for i in range(index):
                aux = aux.proximo
            return aux.valor


    