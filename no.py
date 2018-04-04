# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from tabuleiro import Tabuleiro as Tab

class No(object):
    def __init__(self, tabuleiro, pai=None):
        self.tabuleiro = tabuleiro      # tabela do jogo
        self.valor = None               # valor
        self.posicao = None             # verificar uso da posicao
        self.pai = pai                  # nó de referência
        self.filhos = []                # lista de nós filhos

    def setTabuleiro(self, tab):
        self.tabuleiro = tab

    def getTabuleiro(self):
        return self.tabuleiro

    def setValor(self,val):
        self.valor = val

    def getValor(self):
        return self.valor

    def setPosicao(self, pos):
        self.posicao = pos

    def getPosicao(self):
        return self.posicao

    def setPai(self, pai):
        self.pai = pai

    def getPai(self):
        return self.pai

    def addFilho(self, noFilho):
        self.filhos.append(noFilho)
    
    def getFihos(self):
        return self.filhos
  

if __name__ == "__main__":
    meuno = No(2, 3)
    meuno.addFilho(No(Tab([[1, 3, 2], [4, 5, 5], [6, 7, 8]]), meuno))
    meuno.addFilho(No(Tab([[6, 6, 6], [4, 5, 5], [6, 7, 8]]), meuno))

    for ele in meuno.filhos:
        print(ele.tabuleiro.show())
