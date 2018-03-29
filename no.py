# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

class No:
    def __init__(self, tabela, valor=0, pai=None):
        self.tabela = tabela    # tabela do jogo
        self.valor = valor      # valor
        self.pai = pai          # nó de referência
        self.filhos = []        # lista de nós filhos

    def addFilho(self, noFilho):
        self.filhos.append(noFilho)
