# -*- coding: utf-8 -*-

# DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from point import Point
from no import No
from tabuleiro import Tabuleiro as Tab
from arvore import Arvore as Arv
import copy
import random

from math import inf


class JVelha(object):

    def __init__(self):
        self.tab = Tab(None)
        self.contJog = 0
        self.jogador = None  # humano -1 | pc +1
        self.nivel = None

    def addContJog(self):
        self.contJog += 1

    def zerarContJog(self):
        self.contJog = 0

    def getContJog(self):
        return self.contJog

    def getTabuleiro(self):
        return self.tab

    def setNivel(self, nivel):
        self.nivel = nivel

    def getNivel(self):
        return self.nivel

    def setJogador(self, jogador):
        self.jogador = jogador

    def getJogador(self):
        return self.jogador

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

    def vencedor(self, tab, jogador):

        vencer = [[tab.getLocal(Point(0, 0)), tab.getLocal(Point(0, 1)), tab.getLocal(Point(0, 2))],
                  [tab.getLocal(Point(1, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(1, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(2, 1)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 0)), tab.getLocal(Point(2, 0))],
                  [tab.getLocal(Point(0, 1)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 1))],
                  [tab.getLocal(Point(0, 2)), tab.getLocal(Point(1, 2)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(0, 2))]]

        opcao = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6])

        for indice, valor in enumerate(vencer):
            if [jogador, jogador, jogador] == valor:
                return opcao[indice]

    def alinhamento(self, tab, player):

        # adiciona o seu valor às celulas vazias
        for item in tab.getNone():              # lista de None points
            tab.setLocal(item, player)

        # verificar alinhamentos
        vencer = [[tab.getLocal(Point(0, 0)), tab.getLocal(Point(0, 1)), tab.getLocal(Point(0, 2))],
                  [tab.getLocal(Point(1, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(1, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(2, 1)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 0)), tab.getLocal(Point(2, 0))],
                  [tab.getLocal(Point(0, 1)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 1))],
                  [tab.getLocal(Point(0, 2)), tab.getLocal(Point(1, 2)), tab.getLocal(Point(2, 2))],

                  [tab.getLocal(Point(0, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(2, 2))],
                  [tab.getLocal(Point(2, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(0, 2))]]

        alinhamento = 0

        for indice, valor in enumerate(vencer):
            if [player, player, player] == valor:
                alinhamento += player

        return alinhamento


    def heuristica(self, tab):

        score = self.alinhamento(copy.deepcopy(tab), 1)
        score += self.alinhamento(copy.deepcopy(tab), -1)

        return score
            

    def hardrules(self, tab):
        print("Ganhar")
        #Tentar sempre ganhar
        for item in tab.getNone():  # lista de None points    
            tab.setLocal(item,1)
            if self.isVencedor(tab, 1)==True:
                tab.setLocal(item,None)
                return item
            tab.setLocal(item, None)

        print("Bloquear")
        #Bloquear o adversário
        for item in tab.getNone():  # lista de None points
            tab.setLocal(item, -1)
            if self.isVencedor(tab, -1) == True:
                tab.setLocal(item, None)
                return item   
            tab.setLocal(item, None)

        #Bloquear triâgulos em torno do centro e cantos

        print("Triangulos 1")

        if ((tab.getLocal(Point(0, 0)) == -1 and tab.getLocal(Point(2, 2)) == -1) or 
            (tab.getLocal(Point(2, 0)) == -1 and tab.getLocal(Point(0, 2)) == -1)) and (tab.getLocal(Point(1, 1)) == 1):
            print("\n entrei!")
            return random.choice([Point(0,1), Point(1,0), Point(1,2), Point(2,1)])

        print("Triangulos 2")

        if (tab.getLocal(Point(0, 1)) == -1 or tab.getLocal(Point(1, 0)) == -1) and tab.getLocal(Point(0,0))==None:
            return Point(0,0)
        elif (tab.getLocal(Point(0,1)) == -1 or tab.getLocal(Point(1,2)) == -1) and tab.getLocal(Point(0,2))==None:
            return Point(0,2)
        elif (tab.getLocal(Point(1,0)) == -1 or tab.getLocal(Point(2,1)) == -1) and tab.getLocal(Point(2,0))==None:
            return Point(2,0)
        elif (tab.getLocal(Point(1,2)) == -1 or tab.getLocal(Point(2,1)) == -1) and tab.getLocal(Point(2,2))==None:
            return Point(2,2)
         
        print("None")
        return None

    def minimax(self, tab, prof, player):

        if player == 1:  # 1 PC | -1 HUMANO
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if prof == 0 or self.isVencedor(tab, 1) or self.isVencedor(tab, -1) or len(self.tab.getNone()) == 0:
            score = self.heuristica(tab)
            return [-1, -1, score]

        for item in tab.getNone():  # lista de None points

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

        return best  # retorna x y score


if __name__ == "__main__":

    jogo = JVelha()
    #casa1 = []
    # casa1 = jogo.minimax(Tab([[1, None, -1], [None, -1, None], [1, -1, None]]), 2, 1)  # Tab([[1, -1, -1], [1, -1, -1], [1, 1, -1]]), 2, 1)
    #print(casa1[0], " ", casa1[1], " ", casa1[2])

    ff = jogo.vencedor(Tab([[1, None, -1], [1, -1, None], [1, -1, None]]), 1)

    print(ff)
