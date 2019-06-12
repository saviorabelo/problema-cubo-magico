# -*- coding: utf-8 -*-

import numpy as np
from no import No
from gerarEstadoInicial import gerarEstadoInicial
from estadosFinais import estadosFinais
from funcaoCusto import funcaoCusto
from funcaoSucessora import funcaoSucessora

class ProblemaCubo(object):
    
    def __init__(self, numero):
        estadoInicial = gerarEstadoInicial(numero)
        self.Inicio = No(estadoInicial)
    #Fim da Função
    
    def acoes(self, acao):
        #acoes = np.array(['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha'])
        
        
        if(acao == 'R'):
            aux = ['R','L','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'Rlinha'):
            aux = ['Rlinha','Llinha','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'L'):
            aux = ['R','L','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'Llinha'):
            aux = ['Rlinha','Llinha','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'U'):
            aux = ['R','Rlinha','L','Llinha','U','D','F','Flinha','B','Blinha']
        elif(acao == 'Ulinha'):
            aux = ['R','Rlinha','L','Llinha','Ulinha','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'D'):
            aux = ['R','Rlinha','L','Llinha','U','D','F','Flinha','B','Blinha']
        elif(acao == 'Dlinha'):
            aux = ['R','Rlinha','L','Llinha','Ulinha','Dlinha','F','Flinha','B','Blinha']
        elif(acao == 'F'):
            aux = ['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','F','B']
        elif(acao == 'Flinha'):
            aux = ['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','Flinha','Blinha']
        elif(acao == 'B'):
            aux = ['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','F','B']
        elif(acao == 'Blinha'):
            aux = ['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','Flinha','Blinha']
        elif(acao == None):
            aux = ['R','Rlinha','L','Llinha','U','Ulinha','D','Dlinha','F','Flinha','B','Blinha']
        else:
            aux = []
            print('Acão inesistente!')
        return aux
        
        
        #aux = np.array(['R','L','U','D','F','B'])
        #return aux
    #Fim da Função
        
        
    def funcaoSucessora(self, estadoAtual,acao):
        #Chamada da função sucessora
        return funcaoSucessora(estadoAtual,acao)
        
        
    def testeObjetivo(self, estado):
        aux = funcaoCusto(estado)
        if(aux == 0):
            return True
        return False
    #Fim da Função