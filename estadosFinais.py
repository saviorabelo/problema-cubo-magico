# -*- coding: utf-8 -*-
from funcaoSucessora import *

#Início da função
def estadosFinais():
    #Gera todas as combinações(24) do objetivo do cubo mágico 2x2
    
    #1º foi fixado o cubo da seguinte forma:
    #Face branca em baixo e face azul na frente, consequentemente, a 
    #face amarela ficou em cima.
    
    ##Esses estados são todos com a face azul na frente e a face verde atrás
    
    #O estado11 é o estado descrito acima(face amarela em acima)
    '''
    estado11 = np.matrix([[0, 0, 1, 2, 0, 0],
                          [0, 0, 3, 4, 0, 0],
                          [5, 6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15, 16],
                          [0, 0, 17, 18, 0, 0],
                          [0, 0, 19, 20, 0, 0],
                          [0, 0, 21, 22, 0, 0],
                          [0, 0, 23, 24, 0, 0]])
    '''
    estado11 = np.matrix([['0', '0', 'a1', 'a2', '0', '0'],
                          ['0', '0', 'a3', 'a4', '0', '0'],
                          ['b1', 'b2', 'c1', 'c2', 'd1', 'd2'],
                          ['b3', 'b4', 'c3', 'c4', 'd3', 'd4'],
                          ['0', '0', 'e1', 'e2', '0', '0'],
                          ['0', '0', 'e3', 'e4', '0', '0'],
                          ['0', '0', 'f1', 'f2', '0', '0'],
                          ['0', '0', 'f3', 'f4', '0', '0']])    
    
    #O estado12 é o estado11 com uma rotação de 90 graus(face roxa em acima)
    estado12 = funcaoSucessora(estado11,'F')
    estado12 = funcaoSucessora(estado12,'Blinha')
    #print(estado12)
    
    #O estado13 é o estado12 com uma rotação de 90 graus(face branca em acima)
    estado13 = funcaoSucessora(estado12,'F')
    estado13 = funcaoSucessora(estado13,'Blinha')
    #print(estado13)
    
    #O estado14 é o estado13 com uma rotação de 90 graus(face vermelha em acima)
    estado14 = funcaoSucessora(estado13,'F')
    estado14 = funcaoSucessora(estado14,'Blinha')
    #print(estado14)
    
    ##Esses estados são todos com a face branca na frente e a face amarela atrás
    
    #O estado21 é o estado descrito acima(face azul em acima)
    estado21 = funcaoSucessora(estado11,'R')
    estado21 = funcaoSucessora(estado21,'Llinha')
    #print(estado21)
    
    #O estado22 é o estado21 com uma rotação de 90 graus(face roxa em acima) 
    estado22 = funcaoSucessora(estado21,'F')
    estado22 = funcaoSucessora(estado22,'Blinha')
    #print(estado22)
    
    #O estado23 é o estado22 com uma rotação de 90 graus(face verde em acima) 
    estado23 = funcaoSucessora(estado22,'F')
    estado23 = funcaoSucessora(estado23,'Blinha')
    #print(estado23)
    
    #O estado24 é o estado23 com uma rotação de 90 graus(face vermelho em acima) 
    estado24 = funcaoSucessora(estado23,'F')
    estado24 = funcaoSucessora(estado24,'Blinha')
    #print(estado24)
    
    ##Esses estados são todos com a face verde na frente e a face azul atrás
    
    #O estado31 é o estado descrito acima(face branca em acima)
    estado31 = funcaoSucessora(estado11,'R')
    estado31 = funcaoSucessora(estado31,'R')
    estado31 = funcaoSucessora(estado31,'Llinha')
    estado31 = funcaoSucessora(estado31,'Llinha')
    #print(estado31)
    
    #O estado32 é o estado31 com uma rotação de 90 graus(face roxa em acima) 
    estado32 = funcaoSucessora(estado31,'F')
    estado32 = funcaoSucessora(estado32,'Blinha')
    #print(estado32)
    
    #O estado33 é o estado32 com uma rotação de 90 graus(face amarela em acima) 
    estado33 = funcaoSucessora(estado32,'F')
    estado33 = funcaoSucessora(estado33,'Blinha')
    #print(estado33)
    
    #O estado34 é o estado33 com uma rotação de 90 graus(face vermelha em acima) 
    estado34 = funcaoSucessora(estado33,'F')
    estado34 = funcaoSucessora(estado34,'Blinha')
    #print(estado34)
    
    ##Esses estados são todos com a face amarela na frente e a face branca atrás
    
    #O estado41 é o estado descrito acima(face verde em acima)
    estado41 = funcaoSucessora(estado11,'Rlinha')
    estado41 = funcaoSucessora(estado41,'L')
    #print(estado41)
    
    #O estado42 é o estado41 com uma rotação de 90 graus(face roxa em acima) 
    estado42 = funcaoSucessora(estado41,'F')
    estado42 = funcaoSucessora(estado42,'Blinha')
    #print(estado42)
    
    #O estado43 é o estado42 com uma rotação de 90 graus(face azul em acima) 
    estado43 = funcaoSucessora(estado42,'F')
    estado43 = funcaoSucessora(estado43,'Blinha')
    #print(estado43)
    
    #O estado44 é o estado33 com uma rotação de 90 graus(face vermelha em acima) 
    estado44 = funcaoSucessora(estado43,'F')
    estado44 = funcaoSucessora(estado44,'Blinha')
    #print(estado44)
    
    ##Esses estados são todos com a face roxa na frente e a face vermelha atrás
    
    #O estado51 é o estado descrito acima(face amarela em acima)
    estado51 = funcaoSucessora(estado11,'Ulinha')
    estado51 = funcaoSucessora(estado51,'D')
    #print(estado51)
    
    #O estado52 é o estado51 com uma rotação de 90 graus(face verde em acima) 
    estado52 = funcaoSucessora(estado51,'F')
    estado52 = funcaoSucessora(estado52,'Blinha')
    #print(estado52)
    
    #O estado53 é o estado52 com uma rotação de 90 graus(face branca em acima) 
    estado53 = funcaoSucessora(estado52,'F')
    estado53 = funcaoSucessora(estado53,'Blinha')
    #print(estado53)
    
    #O estado54 é o estado53 com uma rotação de 90 graus(face azul em acima) 
    estado54 = funcaoSucessora(estado53,'F')
    estado54 = funcaoSucessora(estado54,'Blinha')
    #print(estado54)
    
    ##Esses estados são todos com a face vermelha na frente e a face roxa atrás
    
    #O estado61 é o estado descrito acima(face amarela em acima)
    estado61 = funcaoSucessora(estado11,'U')
    estado61 = funcaoSucessora(estado61,'Dlinha')
    #print(estado61)
    
    #O estado62 é o estado61 com uma rotação de 90 graus(face azul em acima) 
    estado62 = funcaoSucessora(estado61,'F')
    estado62 = funcaoSucessora(estado62,'Blinha')
    #print(estado62)
    
    #O estado53 é o estado52 com uma rotação de 90 graus(face branca em acima) 
    estado63 = funcaoSucessora(estado62,'F')
    estado63 = funcaoSucessora(estado63,'Blinha')
    #print(estado63)
    
    #O estado64 é o estado53 com uma rotação de 90 graus(face verde em acima) 
    estado64 = funcaoSucessora(estado63,'F')
    estado64 = funcaoSucessora(estado64,'Blinha')
    #print(estado64)
    
    
    todosEstadosObjetivo = ([estado11]+[estado12]+[estado13]+[estado14]+
                            [estado21]+[estado22]+[estado23]+[estado24]+
                            [estado31]+[estado32]+[estado33]+[estado34]+
                            [estado41]+[estado42]+[estado43]+[estado44]+
                            [estado51]+[estado52]+[estado53]+[estado54]+
                            [estado61]+[estado62]+[estado63]+[estado64])
    #print(todosEstadosObjetivo)
    
    #todosEstadosObjetivo = ([estado11])    
    
    return todosEstadosObjetivo
#Fim da função

'''
#Inicio da função
def funcaoObjetivo(estado):
    
    for i in todosEstadosObjetivo:
        if(np.array_equal(estado, i)):
            return True
    return False
#Fim da função

#Teste
#print(funcaoObjetivo(estado11))
'''