from No import No

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0


    def inserir(self, valor):
        no = No(valor)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1


    def remover(self):
        if self.tamanho == 0:
            return print("Erro: pilha já está vazia")
        aux = self.topo
        self.topo = aux.proximo
        self.tamanho -= 1


    def observar_pilha(self):
        if self.tamanho == 0:
            return ''
        return self.topo.valor


    def __len__(self):
        return self.tamanho
    

    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        if self.tamanho > 0:
            r = ""
            aux = self.topo
            while aux:
                if aux.proximo is None:
                    r += str(aux.valor)
                    break
                r += str(aux.valor) + "\n"
                aux = aux.proximo
            return r
        else:
            return "lista vazia"
