# -*- coding: utf-8 -*-

class No:

    def __init__(self, estado):
        
        self.estado = estado
        self.pai = None
        self.profundidade = 0
        self.custo = 0
        self.acao = None
        
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def setPai(self, pai):
        self.pai = pai
        
    def getPai(self):
        return self.pai
    
    def setProfundidade(self, profundidade):
        self.profundidade = profundidade

    def getProfundidade(self):
        return self.profundidade
    
    def setCusto(self, custo):
        self.custo = custo

    def getCusto(self):
        return self.custo
    
    def setAcao(self, acao):
        self.acao = acao

    def getAcao(self):
        return self.acao

    def printar(self):
        print('Estado:\n', self.estado, '\nPai:', self.pai, '\nCusto:', self.custo, '\nAcao:', self.acao, '\nProfundidade:', self.profundidade)
        
    
    
    