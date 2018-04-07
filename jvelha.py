# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from point import Point
from no import No
from tabuleiro import Tabuleiro as Tab
from arvore import Arvore as Arv

class JVelha(object):
        
    def __init__(self):
        self.tab = Tab(None)
        self.contJog = 0

    def addContJog(self):
        self.contJog += 1

    def zerarContJog(self):
        self.contJog = 0

    def getContJog(self):
        return self.contJog

    def getTabuleiro(self):
        return self.tab        

    def minmax(self, jogador):
        #TODO chamar a tabela do proprio jogo como raiz para o metodo

        return 1

    def isVencedor(self, jogador):
        
        vencer = [[None, None, None], [None, None, None], [None, None, None]]

        vencer = [[self.tab.getLocal(Point(0,0)), self.tab.getLocal(Point(0,1)), self.tab.getLocal(Point(0,2))],
                  [self.tab.getLocal(Point(1,0)), self.tab.getLocal(Point(1,1)), self.tab.getLocal(Point(1,2))],
                  [self.tab.getLocal(Point(2,0)), self.tab.getLocal(Point(2,1)), self.tab.getLocal(Point(2,2))],

                  [self.tab.getLocal(Point(0,0)), self.tab.getLocal(Point(1,0)), self.tab.getLocal(Point(2,0))],
                  [self.tab.getLocal(Point(0,1)), self.tab.getLocal(Point(1,1)), self.tab.getLocal(Point(2,1))],
                  [self.tab.getLocal(Point(0,2)), self.tab.getLocal(Point(1,2)), self.tab.getLocal(Point(2,2))],
                  
                  [self.tab.getLocal(Point(0,0)), self.tab.getLocal(Point(1,1)), self.tab.getLocal(Point(2,2))],
                  [self.tab.getLocal(Point(2,0)), self.tab.getLocal(Point(1,1)), self.tab.getLocal(Point(0,2))]]

        if [jogador, jogador, jogador] in vencer:
            return True
        else:
            return False