# -*- coding: utf-8 -*-
import numpy as np

#Chamada em problemaCubo

#Inicio da função
def funcaoSucessora(estadoAtual,acao):
    
    novoEstado = np.copy(estadoAtual)
    
    #Direita horário
    if(acao == 'R'):
        novoEstado[0,3] = estadoAtual[6,3]
        novoEstado[1,3] = estadoAtual[7,3]
        novoEstado[2,3] = estadoAtual[0,3]
        novoEstado[3,3] = estadoAtual[1,3]
        novoEstado[4,3] = estadoAtual[2,3]
        novoEstado[5,3] = estadoAtual[3,3]
        novoEstado[6,3] = estadoAtual[4,3]
        novoEstado[7,3] = estadoAtual[5,3]
        novoEstado[2,4] = estadoAtual[2,5]
        novoEstado[2,5] = estadoAtual[3,5]
        novoEstado[3,4] = estadoAtual[2,4]
        novoEstado[3,5] = estadoAtual[3,4]
    
    #Direita anti-horário
    elif(acao == 'Rlinha'):
        novoEstado[0,3] = estadoAtual[2,3]
        novoEstado[1,3] = estadoAtual[3,3]
        novoEstado[2,3] = estadoAtual[4,3]
        novoEstado[3,3] = estadoAtual[5,3]
        novoEstado[4,3] = estadoAtual[6,3]
        novoEstado[5,3] = estadoAtual[7,3]
        novoEstado[6,3] = estadoAtual[0,3]
        novoEstado[7,3] = estadoAtual[1,3]
        novoEstado[2,4] = estadoAtual[3,4]
        novoEstado[2,5] = estadoAtual[2,4]
        novoEstado[3,4] = estadoAtual[3,5]
        novoEstado[3,5] = estadoAtual[2,5]
    
    elif(acao == 'L'):
        novoEstado[0,2] = estadoAtual[2,2]
        novoEstado[1,2] = estadoAtual[3,2]
        novoEstado[2,2] = estadoAtual[4,2]
        novoEstado[3,2] = estadoAtual[5,2]
        novoEstado[4,2] = estadoAtual[6,2]
        novoEstado[5,2] = estadoAtual[7,2]
        novoEstado[6,2] = estadoAtual[0,2]
        novoEstado[7,2] = estadoAtual[1,2]
        novoEstado[2,0] = estadoAtual[2,1]
        novoEstado[2,1] = estadoAtual[3,1]
        novoEstado[3,0] = estadoAtual[2,0]
        novoEstado[3,1] = estadoAtual[3,0]

    elif(acao == 'Llinha'):
        novoEstado[0,2] = estadoAtual[6,2]
        novoEstado[1,2] = estadoAtual[7,2]
        novoEstado[2,2] = estadoAtual[0,2]
        novoEstado[3,2] = estadoAtual[1,2]
        novoEstado[4,2] = estadoAtual[2,2]
        novoEstado[5,2] = estadoAtual[3,2]
        novoEstado[6,2] = estadoAtual[4,2]
        novoEstado[7,2] = estadoAtual[5,2]
        novoEstado[2,0] = estadoAtual[3,0]
        novoEstado[2,1] = estadoAtual[2,0]
        novoEstado[3,0] = estadoAtual[3,1]
        novoEstado[3,1] = estadoAtual[2,1]     

    elif(acao == 'U'):
        novoEstado[3,0] = estadoAtual[5,3]
        novoEstado[2,0] = estadoAtual[5,2]
        novoEstado[0,2] = estadoAtual[3,0]
        novoEstado[0,3] = estadoAtual[2,0]
        novoEstado[2,5] = estadoAtual[0,2]
        novoEstado[3,5] = estadoAtual[0,3]
        novoEstado[5,2] = estadoAtual[3,5]
        novoEstado[5,3] = estadoAtual[2,5]
        novoEstado[6,2] = estadoAtual[6,3]
        novoEstado[6,3] = estadoAtual[7,3]
        novoEstado[7,2] = estadoAtual[6,2]
        novoEstado[7,3] = estadoAtual[7,2]    

    elif(acao == 'Ulinha'):
        novoEstado[3,0] = estadoAtual[0,2]
        novoEstado[2,0] = estadoAtual[0,3]
        novoEstado[0,2] = estadoAtual[2,5]
        novoEstado[0,3] = estadoAtual[3,5]
        novoEstado[2,5] = estadoAtual[5,3]
        novoEstado[3,5] = estadoAtual[5,2]
        novoEstado[5,2] = estadoAtual[2,0]
        novoEstado[5,3] = estadoAtual[3,0]
        novoEstado[6,2] = estadoAtual[7,2]
        novoEstado[6,3] = estadoAtual[6,2]
        novoEstado[7,2] = estadoAtual[7,3]
        novoEstado[7,3] = estadoAtual[6,3]     
    
    elif(acao == 'D'):
        novoEstado[3,1] = estadoAtual[1,2]
        novoEstado[2,1] = estadoAtual[1,3]
        novoEstado[1,2] = estadoAtual[2,4]
        novoEstado[1,3] = estadoAtual[3,4]
        novoEstado[2,4] = estadoAtual[4,3]
        novoEstado[3,4] = estadoAtual[4,2]
        novoEstado[4,2] = estadoAtual[2,1]
        novoEstado[4,3] = estadoAtual[3,1]
        novoEstado[2,2] = estadoAtual[2,3]
        novoEstado[2,3] = estadoAtual[3,3]
        novoEstado[3,2] = estadoAtual[2,2]
        novoEstado[3,3] = estadoAtual[3,2]    
    
    elif(acao == 'Dlinha'):
        novoEstado[3,1] = estadoAtual[4,3]
        novoEstado[2,1] = estadoAtual[4,2]
        novoEstado[1,2] = estadoAtual[3,1]
        novoEstado[1,3] = estadoAtual[2,1]
        novoEstado[2,4] = estadoAtual[1,2]
        novoEstado[3,4] = estadoAtual[1,3]
        novoEstado[4,2] = estadoAtual[3,4]
        novoEstado[4,3] = estadoAtual[2,4]
        novoEstado[2,2] = estadoAtual[3,2]
        novoEstado[2,3] = estadoAtual[2,2]
        novoEstado[3,2] = estadoAtual[3,3]
        novoEstado[3,3] = estadoAtual[2,3]      
    
    elif(acao == 'F'):
        novoEstado[3,0] = estadoAtual[3,2]
        novoEstado[3,1] = estadoAtual[3,3]
        novoEstado[3,2] = estadoAtual[3,4]
        novoEstado[3,3] = estadoAtual[3,5]
        novoEstado[3,4] = estadoAtual[6,3]
        novoEstado[3,5] = estadoAtual[6,2]
        novoEstado[4,2] = estadoAtual[4,3]
        novoEstado[4,3] = estadoAtual[5,3]
        novoEstado[5,2] = estadoAtual[4,2]
        novoEstado[5,3] = estadoAtual[5,2]
        novoEstado[6,2] = estadoAtual[3,1]
        novoEstado[6,3] = estadoAtual[3,0]    
    
    elif(acao == 'Flinha'):
        novoEstado[3,0] = estadoAtual[6,3]
        novoEstado[3,1] = estadoAtual[6,2]
        novoEstado[3,2] = estadoAtual[3,0]
        novoEstado[3,3] = estadoAtual[3,1]
        novoEstado[3,4] = estadoAtual[3,2]
        novoEstado[3,5] = estadoAtual[3,3]
        novoEstado[4,2] = estadoAtual[5,2]
        novoEstado[4,3] = estadoAtual[4,2]
        novoEstado[5,2] = estadoAtual[5,3]
        novoEstado[5,3] = estadoAtual[4,3]
        novoEstado[6,2] = estadoAtual[3,5]
        novoEstado[6,3] = estadoAtual[3,4]      
    
    elif(acao == 'B'):
        novoEstado[0,2] = estadoAtual[0,3]
        novoEstado[0,3] = estadoAtual[1,3]
        novoEstado[1,2] = estadoAtual[0,2]
        novoEstado[1,3] = estadoAtual[1,2]
        novoEstado[2,0] = estadoAtual[7,3]
        novoEstado[2,1] = estadoAtual[7,2]
        novoEstado[2,2] = estadoAtual[2,0]
        novoEstado[2,3] = estadoAtual[2,1]
        novoEstado[2,4] = estadoAtual[2,2]
        novoEstado[2,5] = estadoAtual[2,3]
        novoEstado[7,2] = estadoAtual[2,5]
        novoEstado[7,3] = estadoAtual[2,4]    
    
    elif(acao == 'Blinha'):
        novoEstado[0,2] = estadoAtual[1,2]
        novoEstado[0,3] = estadoAtual[0,2]
        novoEstado[1,2] = estadoAtual[1,3]
        novoEstado[1,3] = estadoAtual[0,3]
        novoEstado[2,0] = estadoAtual[2,2]
        novoEstado[2,1] = estadoAtual[2,3]
        novoEstado[2,2] = estadoAtual[2,4]
        novoEstado[2,3] = estadoAtual[2,5]
        novoEstado[2,4] = estadoAtual[7,3]
        novoEstado[2,5] = estadoAtual[7,2]
        novoEstado[7,2] = estadoAtual[2,1]
        novoEstado[7,3] = estadoAtual[2,0] 
    
    else:
        print('Ação não existente!')
        return []
    
    return novoEstado
#Fim da função