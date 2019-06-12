from no import No
# -*- coding: utf-8 -*-
import numpy as np

#Inicio da classe
class FilaDePrioridade:
    
    def __init__(self):
        self.list = []

    def adicionar(self,item):
        self.list.append(item)

    def vazia(self):
        return (len(self.list) == 0)

    def __contains__(self, item):
        return (item in self.list)
    
    #Remove sempre o nó de menor custo
    def remove(self):
        menori = 0
        for i in range(1,len(self.list)):
            if (self.list[i].custo < self.list[menori].custo):
                menori = i
        item = self.list[menori]
        self.list[menori:menori+1] = []
        return item
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
    
    def tamanho(self):
        return len(self.list)
    
    def retira(self, indice):
        return self.list.pop(indice)
    
    def __iter__(self):
        for x in self.list:
            yield x    
#Fim da classe

#Inicio da classe
class Fila:
    def __init__(self):
        self.list = []
        
    #Insere no final
    def adicionar(self,item):
        self.list.append(item)
    
    #Remove no começo
    def remove(self):
        return self.list.pop(0)

    def vazia(self):
        return len(self.list) == 0

    def __contains__(self, item):
        return item in self.list
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
#Fim da classe

#Inicio da classe
class Pilha:
    def __init__(self):
        self.list = []
    
    #Insere no final
    def adicionar(self,item):
        self.list.append(item)
    
    #Remove no final
    def remove(self):
        return self.list.pop()

    def vazia(self):
        return len(self.list) == 0

    def __contains__(self, item):
        return item in self.list
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
#Fim da classe

'''
#Testes
teste = FilaDePrioridade()
teste.adicionar(5)
teste.adicionar(9)
teste.adicionar(4)
teste.adicionar(1)
teste.printar()

a = teste.remove()

print(teste.vazia())

matriz1 = np.matrix([['0', '0', 'a1', 'a2', '0', '0'],
                      ['0', '0', 'a3', 'a4', '0', '0'],
                      ['b1', 'b2', 'c1', 'c2', 'd1', 'd2'],
                      ['b3', 'b4', 'c3', 'c4', 'd3', 'd4'],
                      ['0', '0', 'e1', 'e2', '0', '0'],
                      ['0', '0', 'e3', 'e4', '0', '0'],
                      ['0', '0', 'f1', 'f2', '0', '0'],
                      ['0', '0', 'f3', 'f4', '0', '0']])

no1 = No(matriz1)
no1.setCusto(5)

no2 = No(matriz1)
no2.setCusto(10)

no3 = No(matriz1)
no3.setCusto(1)

no4 = No(matriz1)
no4.setCusto(15)

borda = FilaDePrioridade()
borda.adicionar(no1)
borda.adicionar(no2)
borda.adicionar(no3)
borda.adicionar(no4)

#borda.printar()

aux = borda.remove()
#borda.printar()

print(no3 in borda)
'''