# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from no import No
from tabuleiro import Tabuleiro as Tab

class Arvore(object):
    def __init__(self, noRaiz):
        self.raiz = noRaiz  # nó raiz da árvore
        self.prof = None    # profundidade da árvore

    def gerarArvore(self, raiz, noh, prof):
    

        '''         if prof==0 or prof == None:
            print("A raiz é a própria árvore.")
            return 
        else:
            listNone = noh.tabuleiro.getNone()

            for item in listNone:
                #tabuleiro add tag e pai           
                auxTab = noh.tabuleiro

                #como sempre a raiz é o computador, então toda profundidade par é 'O' e impar é 'X'
                auxTab.setLocal(item, prof % 2 == 0 and "O" or "X")

                auxNo = No(auxTab,noh)
                auxNo.setPosicao(item)

                noh.addFilho(auxNo) '''
               
            #TODO acrescentar mais uma linha de addFilho()        

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
