# -*- coding: utf-8 -*-
from funcaoSucessora import *
import numpy as np

#Início da função
def todosEstadosIguais(estado):
    
    estado11 = np.copy(estado)
    
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
    
    
    todosEstadosIguais = ([estado11]+[estado12]+[estado13]+[estado14]+
                          [estado21]+[estado22]+[estado23]+[estado24]+
                          [estado31]+[estado32]+[estado33]+[estado34]+
                          [estado41]+[estado42]+[estado43]+[estado44]+
                          [estado51]+[estado52]+[estado53]+[estado54]+
                          [estado61]+[estado62]+[estado63]+[estado64])
    #print(todosEstadosIguais)
   
    
    return todosEstadosIguais
#Fim da função