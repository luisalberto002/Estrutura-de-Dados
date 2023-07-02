from No import No

class Arvore_Binaria:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
            self.tamanho += 1
            return
        aux = self.raiz
        while aux:
            if valor < aux.valor:
                if aux.esquerda is None:
                    aux.esquerda = No(valor)
                    self.tamanho += 1
                    return
                aux = aux.esquerda
            elif valor > aux.valor:
                if aux.direita is None:
                    aux.direita = No(valor)
                    self.tamanho += 1
                    return
                aux = aux.direita
            else:
                print(f'O valor {valor} já foi adicionado')
                return

    
    def remover(self, valor):
        self.raiz = self.remover_recursivo(self.raiz, valor)
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

    def maximo(self,no=None):
        if no is None:
            no = self.raiz
        while no.direita:
            no = no.direita
        return no.valor


    def altura(self,no=None):
        if no is None:
            return -1
        else:
            altura_esquerda = self.altura(no.esquerda)
            altura_direita = self.altura(no.direita)
            altura_atual = max(altura_esquerda, altura_direita) + 1
            return altura_atual           
    
    def __len__(self):
        return self.tamanho


    def balancear(self):
        pass

    def p(self, no):
        if no is None:
            return 0
        p_es = 0
        p_di = 0
        if (no.esquerda):
            p_es= self.p(no.esquerda)
        if (no.direita):
            p_di = self.p(no.direita)
        if (p_di > p_es):
            return p_di + 1
        return (p_es + 1)


'''
Fator de balanceamento de um nó
FB = altura(subárvore da esquerda) - altura(subárvore da direita)


'''