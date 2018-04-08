# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from point import Point
from no import No
from tabuleiro import Tabuleiro as Tab
from arvore import Arvore as Arv

from math import inf

class JVelha(object):
        
    def __init__(self):
        self.tab = Tab(None)
        self.contJog = 0
        self.jogador = 1  #humano -1 | pc +1
        self.nivel = 0      

    def addContJog(self):
        self.contJog += 1

    def zerarContJog(self):
        self.contJog = 0

    def getContJog(self):
        return self.contJog

    def getTabuleiro(self):
        return self.tab    

    def setNivel(self, nivel)    :
        self.nivel = nivel

    def getNivel(self):
        return self.getNivel

    def setJogador(self, jogador):
        self.jogador = jogador

    def getJogador(self):
        return self.jogador

    def heuristica(self, tab):

        if self.isVencedor(tab, 1):
            return 1
        elif self.isVencedor(tab, -1):
            return -1
        else:
            return 0

    def isVencedor(self, tab, jogador):

        vencer = [[tab.getLocal(Point(0, 0)), tab.getLocal(Point(0, 1)), tab.getLocal(Point(0, 2))],
                  [tab.getLocal(Point(1, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(1, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(2, 1)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 0)), tab.getLocal(Point(2, 0))],
                  [tab.getLocal(Point(0, 1)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 1))],
                  [tab.getLocal(Point(0, 2)), tab.getLocal(Point(1, 2)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(0, 2))]]

        if [jogador, jogador, jogador] in vencer:
            return True
        else:
            return False

    def minimax(self, tab, prof, player):

        if player == 1: # 1 PC | -1 PESSOA
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if prof == 0 or self.isVencedor(tab, 1) or self.isVencedor(tab, -1):
            score = self.heuristica(tab)
            return [-1, -1, score]

        for item in tab.getNone(): #lista de points

            tab.setLocal(item, player)
            score = self.minimax(tab, prof - 1, -player)
            tab.setLocal(item, None)
            score[0], score[1] = item.x, item.y

            if player == 1:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best     #retorna x y score

    def jogada(self):
        pass
        
        

if __name__ == "__main__":

    jogo = JVelha()
    casa1 = list()
    casa1.append(jogo.minimax(
        Tab([[1, -1, -1], [None, 1, None], [None, None, None]]), 7, 1))

    print(casa1)
