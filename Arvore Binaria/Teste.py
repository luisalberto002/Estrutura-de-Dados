from Arvore_Binaria import *
from tkinter import *

def mostrar_arvore_graficamente(raiz, canvas, x, y, x_dist, y_dist):
    if raiz:
        valor = str(raiz.valor)
        canvas.create_oval(x-15, y-15, x+15, y+15, fill='lightblue')
        canvas.create_text(x, y, text=valor, font=('Arial', 12, 'bold'))
        if raiz.esquerda:
            x_esq = x - x_dist
            y_esq = y + y_dist
            canvas.create_line(x, y+15, x_esq, y_esq-15)
            mostrar_arvore_graficamente(raiz.esquerda, canvas, x_esq, y_esq, x_dist/2, y_dist)
        if raiz.direita:
            x_dir = x + x_dist
            y_dir = y + y_dist
            canvas.create_line(x, y+15, x_dir, y_dir-15)
            mostrar_arvore_graficamente(raiz.direita, canvas, x_dir, y_dir, x_dist/2, y_dist)


#            (5)                       (5)             
#           /   \                    /     \            
#        (3)     (6)              (3)      (7)         
#        / \       \              / \      / \         
#     (1)  (4)     (9)         (1)  (4) (6)  (9)       
#    /  \          /          /  \           /         
#  (0)  (2)      (7)        (0)  (2)       (8)         
#                  \                                 
#                  (8)                             
                                   
# pre-ordem (r,e,d) = 5,3,1,2,4,6,9,7,8
# em-ordem  (e,r,d) = 1,2,3,4,5,6,7,8,9
# pos-ordem (e,d,r) = 2,1,4,3,8,7,9,6,5

#          (9)                         (57)         
#        /     \                     /      \        
#     (4)      (57)                (9)      (78)     
#     /      /     \              /  \      /   \      
#  (1)     (16)     (78)       (4)   (16) (66)  (94)    
#          / \      /  \       /     /  \                 
#       (10) (47) (66)(94)   (1)   (10)(47)               
#                                                 
#                                               
                                   
# pre-ordem (r,e,d) = 9 4 1 57 16 10 47 78 66 94
# em-ordem  (e,r,d) = 1 4 9 10 16 47 57 66 78 94
# pos-ordem (e,d,r) = 1 4 10 47 16 66 94 78 57 9

arvore = Arvore_Binaria()
v1 = [5,3,1,6,9,4,2,7,8,0]
v2 = [9,4,57,16,78,94,1,47,66,10]

for valor in v1:
    arvore.inserir(valor)


print('---' * len(arvore))
arvore.pre_ordem()
arvore.em_ordem()
arvore.pos_ordem()
print('---' * len(arvore))

print(f'Tamanho: {len(arvore)}\nMáximo: {arvore.maximo()}\nMínimo: {arvore.minimo()}\nAltura: {arvore.altura(arvore.raiz)}')


janela = Tk()
janela.title("Árvore de Busca Binária")

canvas_width = 720
canvas_height = 480
canvas = Canvas(janela, width=canvas_width, height=canvas_height)
canvas.pack()

x_inicial = canvas_width // 2
y_inicial = 50
mostrar_arvore_graficamente(arvore.raiz, canvas, x_inicial, y_inicial, x_inicial // 2, 100)

janela.mainloop()
