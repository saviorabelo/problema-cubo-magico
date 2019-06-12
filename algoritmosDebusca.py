# -*- coding: utf-8 -*-
import time
from problemaCubo import ProblemaCubo
from estruturasDeDados import FilaDePrioridade
from estruturasDeDados import Pilha
from estruturasDeDados import Fila
from no import No
from funcaoCusto import funcaoCusto
from todosEstadosIguais import todosEstadosIguais
import numpy as np
import timeit


def aEstrela(N):
    #print('*** Movimentos aleatórios ***')
    problema = ProblemaCubo(N)
    
    noInicial = problema.Inicio
    borda = FilaDePrioridade()
    explorados = []

    borda.adicionar(noInicial)
    
    while not(borda.vazia()):
        no = borda.remove()
        
        #print('------------------------')
        #print('Profundidade do Nó: ',no.getProfundidade())
        #print('Custo do Nó: ',no.getCusto())
        #print('Tamanho da borda: ',borda.tamanho())
        #print('Tamanho da borda: ',len(explorados))
        #print(no.estado)

        if(problema.testeObjetivo(no.estado)):
            return no
        
        explorados.append(no.estado)
        
        for acao in problema.acoes(no.acao):
            
            filho = noFilho(problema, no, acao)        
            
            #if(not compara(filho.estado,explorados)) and (not borda.__contains__(noFilho) and (filho.getProfundidade() <= N)):
            if(not borda.__contains__(filho) and (filho.getProfundidade() <= N)):
                borda.adicionar(filho)
                
            #elif(condicao):
             #   implementar
#Fim da função

#Início da função
def noFilho(problema, pai, acao):
    
    estado = problema.funcaoSucessora(pai.estado, acao)
    no = No(estado)
    no.setProfundidade(pai.profundidade + 1)
    no.setCusto(funcaoCusto(no.estado) + no.getProfundidade())
    no.setAcao(acao)
    no.setPai(pai)
    
    return no
#Término da função

#Funcao para comparar se um estado está na borda
def compara(estado, explorados):
    matrizAux = todosEstadosIguais(estado)
    for matriz in matrizAux:
        for elemento in explorados:
            if(np.array_equal(matriz, elemento)):
                return True
    return False
#Fim da função

#Função para retornar a lista da solução
def solucao(no, move):
    #print(no.getEstado())
    if(no.pai == None):
        return move
    move.append(no.acao)
    #print('Ação do nó: ',no.getAcao())
    aux = solucao(no.pai, move)
    return aux
#Fim da função

#Inicio da função
def busca(N):
    #Começo do tempo
    start = timeit.default_timer()    
    
    #A solução do cubo está em resp(Nó)
    #resp = aEstrela(N)
    #resp = BFS(N)
    #resp = DFS(N)
    resp = IDA(N)
    
    #print(resp.printar())
    
    print('*** Resposta ***')
    aux = solucao(resp,[])
    print(aux[::-1]) #Lista resersa
    
    #Término do tempo
    stop = timeit.default_timer()
    tempo = stop-start
    #print('Tempo: {:f} segundos'.format(tempo))
    
    return tempo #Reorna o tempo em segundos
#Fim da função


#Início da função
def BFS(N):
    print('*** Busca BFS! ***\n')
    
    problema = ProblemaCubo(N)
    
    no = problema.Inicio
    
    if(problema.testeObjetivo(no.estado)):
        print('*** Solução Trivial! ***')
        return no
        
    borda = Fila()
    borda.adicionar(no)
    explorado = []

    while(not borda.vazia()):
        
        #print('*** BORDA ***')
        #borda.printar()
        
        no = borda.remove()
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.acao):
            
            filho = noFilho(problema, no, acao)

            if(not compara(filho.estado,explorado)) and (not borda.__contains__(noFilho)):
                if(problema.testeObjetivo(no.estado)):
                    print('*** Solução Encontrada! ***')
                    return filho
                borda.adicionar(filho)
#Término da função

#Início da função
def DFS(N):
    print('*** Busca DFS! ***\n')
    
    problema = ProblemaCubo(N)
    
    no = problema.Inicio
    
    if(problema.testeObjetivo(no.estado)):
        print('*** Solução Trivial! ***')
        return no
        
    borda = Pilha()
    borda.adicionar(no)
    explorado = []

    while(not borda.vazia()):
        
        #print('*** BORDA ***')
        #borda.printar()
        
        no = borda.remove()
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.acao):
            
            filho = noFilho(problema, no, acao)

            if(not compara(filho.estado,explorado)) and (not borda.__contains__(noFilho)):
                if(problema.testeObjetivo(no.estado)):
                    print('*** Solução Encontrada! ***')
                    return filho
                borda.adicionar(filho)
#Término da função

#Início da função
def IDA(N):
    print('*** Busca IDA! ***\n')
    
    print('*** Movimentos aleatórios ***')
    
    problema = ProblemaCubo(N)
    
    no = problema.Inicio
    
    limite = funcaoCusto(no.estado)
    
    #borda = Pilha()
    
    while(1):
        temp,no = buscaIDA(no, 0, limite, problema)
        
        if(temp == True):
            return no
        
        if(temp == 10000000000000):
            return;
        
        limite = temp
#Término da função

#Início da função
def buscaIDA(no, g, limite, problema):
    
    #Novo Treshold
    f = g + funcaoCusto(no.estado)
    
    #Novo > Antigo
    #Garante que não passa do limite (Cutoff)
    #Poda: Corta o ramo que excedou o threshold
    if(f > limite):
        return f,no
    
    if(problema.testeObjetivo(no.estado)):
        #print('*** Solução Encontrada1! ***')
        return True,no
    
    min = 10000000000000
    
    #Para cada filho
    for acao in problema.acoes(no.acao):
        
        filho = noFilho(problema, no, acao)
        #filho.printar()

            
        temp,auxNo = buscaIDA(filho, g + 5, limite, problema)
        
        if(problema.testeObjetivo(auxNo.estado)):
            #print('*** Solução Encontrada2! ***')
            #print(auxNo.getEstado())
            return True,auxNo
        
        #No final retorna o menor threshold entre os filhos (serao maior que o antigo)
        if(temp < min):
            min = temp
    
    #Novo threshold
    return min,no
#Término da função