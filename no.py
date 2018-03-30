# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

class No(object):
    def __init__(self, tabela, valor=None, pai=None):
        self.tabela = tabela    # tabela do jogo
        self.valor = valor      # valor
        self.posicao = None     # verificar uso da posicao
        self.pai = pai          # nó de referência
        self.filhos = []        # lista de nós filhos

    def addFilho(self, noFilho):
        self.filhos.append(noFilho)
    

if __name__ == "__main__":
    meuno = No(2, 3)
    meuno.addFilho(No(5, 3, meuno))
    print(meuno.filhos[0].tabela)
