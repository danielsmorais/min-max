# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

class Tabuleiro(object):
    
    winner = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]) #lista de winners

    def __init__(self, tabuleiro=[[None, None, None], [None, None, None], [None, None, None]]):
        self.tabuleiro = tabuleiro

    def getTabuleiro(self):
        return self.tabuleiro

    def setTabuleiro(self, tabuleiro):
        self.tabuleiro = tabuleiro

    def setLocal(self,point):
        self.tabuleiro

    def show(self):
        for element in [self.tabuleiro[i:i + 3] for i in range(0, len(self.tabuleiro), 3)]:
            print(element)

    def clear(self):
        self.tabuleiro = [[None, None, None], [None, None, None], [None, None, None]]

        
if __name__ == "__main__":
    ta = [[1, 3, 2], [4, 5, 5], [6, 7, 8]]
    tab = Tabuleiro(ta)
    tab.show()


