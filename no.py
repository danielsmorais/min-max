# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from tabuleiro import Tabuleiro

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
  

''' if __name__ == "__main__":
    meuno = No(2, 3)
    meuno.addFilho(No(5, meuno))
    meuno.addFilho(No(4, meuno))
    print(meuno.filhos[0].tabuleiro)

    for ele in meuno.filhos:
        print(ele.tabuleiro) '''
