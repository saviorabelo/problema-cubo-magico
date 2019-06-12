# -*- coding: utf-8 -*-
import numpy as np
from funcaoSucessora import funcaoSucessora
from estadosFinais import estadosFinais

#A função de custo recebe uma matriz (estado atual do nó)
def funcaoCusto(matriz):

    #Contagem para a cor 1
    cor1 = [matriz[0,2][0],matriz[0,3][0],matriz[1,2][0],matriz[1,3][0]]
    aux = [cor1.count(i) for i in cor1]
    contCor1 = max(aux)
    
    #Contagem para a cor 2
    cor2 = [matriz[2,0][0],matriz[2,1][0],matriz[3,0][0],matriz[3,1][0]]
    aux = [cor2.count(i) for i in cor2]
    contCor2 = max(aux)
    
    #Contagem para a cor 3
    cor3 = [matriz[2,2][0],matriz[2,3][0],matriz[3,2][0],matriz[3,3][0]]
    aux = [cor3.count(i) for i in cor3]
    contCor3 = max(aux)
    
    #Contagem para a cor 4
    cor4 = [matriz[2,4][0],matriz[2,5][0],matriz[3,4][0],matriz[3,5][0]]
    aux = [cor4.count(i) for i in cor4]
    contCor4 = max(aux)
    
    #Contagem para a cor 5
    cor5 = [matriz[4,2][0],matriz[4,3][0],matriz[5,2][0],matriz[5,3][0]]
    aux = [cor5.count(i) for i in cor5]
    contCor5 = max(aux)
    
    #Contagem para a cor 6
    cor6 = [matriz[6,2][0],matriz[6,3][0],matriz[7,2][0],matriz[7,3][0]]
    aux = [cor6.count(i) for i in cor6]
    contCor6 = max(aux)
    
    return (24-(contCor1+contCor2+contCor3+contCor4+contCor5+contCor6))
#Fim da função

'''
matriz = np.matrix([['0', '0', 'a1', 'a2', '0', '0'],
                    ['0', '0', 'a3', 'a4', '0', '0'],
                    ['b1', 'b2', 'c1', 'c2', 'd1', 'd2'],
                    ['b3', 'b4', 'c3', 'c4', 'd3', 'd4'],
                    ['0', '0', 'e1', 'e2', '0', '0'],
                    ['0', '0', 'e3', 'e4', '0', '0'],
                    ['0', '0', 'f1', 'f2', '0', '0'],
                    ['0', '0', 'f3', 'f4', '0', '0']])

teste = estadosFinais()

for matriz in teste:
    print(funcaoCusto(matriz))

#print(matriz)
'''