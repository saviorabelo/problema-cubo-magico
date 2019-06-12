# -*- coding: utf-8 -*-
import numpy as np
from funcaoSucessora import funcaoSucessora

#Inicio da função
def gerarEstadoInicial(N):
    
    acoes = np.array(['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha'])
    #acoes = np.array(['R','L','U','D','F','B'])
    
    '''matriz1 = np.matrix([[0, 0, 1, 2, 0, 0],
                         [0, 0, 3, 4, 0, 0],
                         [5, 6, 7, 8, 9, 10],
                         [11, 12, 13, 14, 15, 16],
                         [0, 0, 17, 18, 0, 0],
                         [0, 0, 19, 20, 0, 0],
                         [0, 0, 21, 22, 0, 0],
                         [0, 0, 23, 24, 0, 0]])'''
    
    matriz1 = np.matrix([['0', '0', 'a1', 'a2', '0', '0'],
                          ['0', '0', 'a3', 'a4', '0', '0'],
                          ['b1', 'b2', 'c1', 'c2', 'd1', 'd2'],
                          ['b3', 'b4', 'c3', 'c4', 'd3', 'd4'],
                          ['0', '0', 'e1', 'e2', '0', '0'],
                          ['0', '0', 'e3', 'e4', '0', '0'],
                          ['0', '0', 'f1', 'f2', '0', '0'],
                          ['0', '0', 'f3', 'f4', '0', '0']])   
    #Número de movimentos
    #N = 5
    
    matriz2 = np.copy(matriz1)
    movimentos = []
    for i in range(N):
        aux = np.random.choice(acoes) #Escolhe aleatório o próximo movimento
        print(aux)
        movimentos.append(aux)
        matriz2 = funcaoSucessora(matriz2,aux)
    
    #print(matriz2)
    return matriz2 #Matriz embaralhada
#Fim da função

#gerarEstadoInicial(5)