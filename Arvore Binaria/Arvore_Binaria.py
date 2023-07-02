from No import No

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            self.balancear()
            self.tamanho += 1
            return
        aux = self.raiz
        while aux:
            if valor < aux.valor:
                if aux.esquerda is None:
                    aux.esquerda = No(valor)
                    self.balancear()
                    self.tamanho += 1
                    return
                aux = aux.esquerda
            elif valor > aux.valor:
                if aux.direita is None:
                    aux.direita = No(valor)
                    self.tamanho += 1
                    self.balancear()
                    return
                aux = aux.direita
            else:
                print(f'O valor {valor} já foi adicionado')
                return

    def remover(self, valor):
        self.raiz = self.remover_recursivo(self.raiz, valor)
        self.balancear()
        self.tamanho -= 1

    def remover_recursivo(self, no, valor):
        if no is None:
            return None
        if valor < no.valor:
            no.esquerda = self.remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            else:
                aux = self.minimo(no.direita)
                no.valor = aux.valor
                no.direita = self.remover_recursivo(no.direita, aux.valor)
        return no

    def buscar(self, valor):
        aux = self.raiz
        while aux:
            if valor == aux.valor:
                return print(f'{aux} encontrado')
            if valor < aux.valor:
                if aux.esquerda is None:
                    return print(f'{valor} não está presente na árvore')
                aux = aux.esquerda
            elif valor > aux.valor:
                if aux.direita is None:
                    return print(f'{valor} não está presente na árvore')
                aux = aux.direita

    def pre_ordem(self):
        print('Pre-ordem:', end=' ')
        self.pre_ordem_percurso(self.raiz)
        print()

    def pre_ordem_percurso(self, no):
        if no is not None:
            print(no, end=' ')
            self.pre_ordem_percurso(no.esquerda)
            self.pre_ordem_percurso(no.direita)

    def em_ordem(self):
        print('Em-ordem:', end=' ')
        self.em_ordem_percurso(self.raiz)
        print()

    def em_ordem_percurso(self, no):
        if no is not None:
            self.em_ordem_percurso(no.esquerda)
            print(no, end=' ')
            self.em_ordem_percurso(no.direita)

    def pos_ordem(self):
        print('Pos-ordem:', end=' ')
        self.pos_ordem_percurso(self.raiz)
        print()

    def pos_ordem_percurso(self, no):
        if no is not None:
            self.pos_ordem_percurso(no.esquerda)
            self.pos_ordem_percurso(no.direita)
            print(no, end=' ')

    def minimo(self, no=None):
        if no is None:
            no = self.raiz
        while no.esquerda:
            no = no.esquerda
        return no.valor

    def maximo(self, no=None):
        if no is None:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.valor

    def altura(self, no=None):
        if no is None:
            return -1
        else:
            altura_es = self.altura(no.esquerda)
            altura_dir = self.altura(no.direita)
            altura_atual = max(altura_es, altura_dir) + 1
            return altura_atual

    def __len__(self):
        return self.tamanho

    def balancear(self):
        self.raiz = self.balancear_recursivo(self.raiz)

    def balancear_recursivo(self, no):
        if no is None:
            return None
        no.esquerda = self.balancear_recursivo(no.esquerda)
        no.direita = self.balancear_recursivo(no.direita)

        fb = self.calcular_fator_balanceamento(no)

        # RSD
        if fb > 1 and self.calcular_fator_balanceamento(no.esquerda) >= 0:
            return self.rotacao_direita(no)

        # RSE
        if fb < -1 and self.calcular_fator_balanceamento(no.direita) <= 0:
            return self.rotacao_esquerda(no)

        # RDD = RSD + RSE
        if fb > 1 and self.calcular_fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        # RDE = RSE + RSD
        if fb < -1 and self.calcular_fator_balanceamento(no.direita) > 0:
            no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def calcular_fator_balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita)

    def rotacao_direita(self, no):
        novo_raiz = no.esquerda
        no.esquerda = novo_raiz.direita
        novo_raiz.direita = no
        return novo_raiz

    def rotacao_esquerda(self, no):
        novo_raiz = no.direita
        no.direita = novo_raiz.esquerda
        novo_raiz.esquerda = no
        return novo_raiz
