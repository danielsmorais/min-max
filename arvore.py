# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from no import No
from tabuleiro import Tabuleiro as Tab

class Arvore(object):
    def __init__(self, noRaiz):
        self.raiz = noRaiz  # nó raiz da árvore
        self.prof = None    # profundidade da árvore

    def gerarArvore(self):
        for ele in self.raiz.filhos:
            ele.addFilho(No(None,None))

        # TODO condicao para verificar se eh possivel ter filhos

        for i in range(self.prof):
            noh = No(Tab(),self.raiz)   # teste
            self.raiz.addFilho()
            
        
        #TODO finalizar a geracao da arvore

    def setRaiz(self,r):
        self.raiz = r

    def getRaiz(self):
        return self.raiz

    def setProf(self, prof):
        self.prof = prof

    def getProf(self):
        return self.prof

    def buscaDFS(self):                
        return 1        


''' if __name__ == "__main__":
    meuno = No(2, 3)
    arv = Arvore(meuno)
    arv.gerarArvore()


    print(arv.raiz.tabuleiro) '''
