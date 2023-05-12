from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0


    def inserir(self, valor):
        no = No(valor)
        if self.tamanho == 0:
            self.inicio = self.fim = no
            self.tamanho += 1
        else:
            self.fim.proximo = no
            self.fim = no
            self.tamanho += 1


    def remover(self):
        if self.tamanho > 0:
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
        else:
            return print("Erro: fila já está vazia")

    
    def observar_fila(self):
        if self.tamanho == 0:
            return ""
        return f'inicio: {self.inicio.valor} fim: {self.fim.valor}'


    def __len__(self):
        return self.tamanho
    

    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        if self.tamanho > 0:
            r = ""
            aux = self.inicio
            while aux:
                if aux.proximo is None:
                    r += str(aux.valor)
                    break
                r += str(aux.valor) + " "
                aux = aux.proximo
            return r
        else:
            return "fila vazia"