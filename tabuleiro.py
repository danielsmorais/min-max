# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from point import Point

class Tabuleiro(object):
    
    def __init__(self, tabuleiro=[[None, None, None], [None, None, None], [None, None, None]]):
        self.tabuleiro = tabuleiro

    def getTabuleiro(self):
        return self.tabuleiro

    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def setLocal(self,point):
        self.tabuleiro

    def addElemento(self, p, ele):
        self.tabuleiro[p.x][p.y] = ele

    def contNone(self):
        cont = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == None:
                    cont += 1
        return cont               
        
    def show(self):
        for element in [self.tabuleiro[i:i + 3] for i in range(0, len(self.tabuleiro), 3)]:
            print(element)

    def clear(self):
        self.tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]

        
if __name__ == "__main__":
    ta = [[1, None, 2], [None, 5, None], [6, 7, None]]
    tab = Tabuleiro(ta)
    tab.show()

    print(tab.contNone())


