# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from point import Point
from no import No
from tabuleiro import Tabuleiro as Tab
from arvore import Arvore as Arv

class JVelha(object):
        
    def __init__(self):
        self.paraVencer = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
        self.tab = Tab()
        self.contJog = 0

    def addContJog(self):
        self.contJog += 1

    def zerarContJog(self):
        self.contJog = 0

    def getContJog(self):
        return self.contJog

    def getTabuleiro(self):
        return self.tab
        

    def minmax(self, id):
        #TODO chamar a tabela do proprio jogo como raiz para o metodo

        return 1

    def isVencedor(self, jogador):
        #TODO chamar a tabela do proprio jogo
        pass
    
        
