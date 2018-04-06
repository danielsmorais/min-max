# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from no import No
from tabuleiro import Tabuleiro as Tab

class Arvore(object):
    def __init__(self, noRaiz):
        self.raiz = noRaiz  # nó raiz da árvore
        self.prof = None    # profundidade da árvore

    def gerarArvore(self):
        
        # TODO condicao para verificar se eh possivel ter filhos

        '''         for i in range(self.prof):
            noh = No(Tab(),self.raiz)   # teste
            self.raiz.addFilho() '''

        if self.prof==0 or self.prof == None:
            print("A raiz é a própria árvore.")
        else:
            contaux = self.raiz.tabuleiro.contNone()
            tabaux = self.raiz.tabuleiro

            tag = 'x'or 'o'

            for i in range(contaux): 
                
                pointaux = tabaux.get1None()
                tabaux.setLocal(pointaux,tag)
                noaux = No(tabaux)
                noaux.setPosicao(pointaux)

                self.raiz.addFilho(noaux,self.raiz)

                #TODO acrescentar mais uma linha de addFilho()
                
            
            
        
        #TODO finalizar a geracao da arvore

    def setRaiz(self,r):
        self.raiz = r

    def getRaiz(self):
        return self.raiz

    def setProf(self,prof):
        self.prof = prof

    def addProf(self):
        self.prof = self.raiz.tabuleiro.contNone()

    def getProf(self):
        return self.prof

    def buscaDFS(self):                
        return 1        


if __name__ == "__main__":
    
    meuno = No(Tab([[1, None, 2], [None, 5, None], [6, 7, None]]))

    arv = Arvore(meuno)

    print(arv.raiz.tabuleiro.contNone())

    for i in range(3):
        arv.raiz.addFilho(No(Tab([[1, 3, 2], [4, 5, 5], [6, 7, 8]]), meuno))

    for i in range(3):
        arv.raiz.filhos[i].tabuleiro.show()
