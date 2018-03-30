# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

from no import No

class Arvore(object):
    def __init__(self, noRaiz):
        self.raiz = noRaiz  # nó raiz da árvore
        self.prof = None    # profundidade da árvore

    def buscaDFS(self):
        
        return 1
        


if __name__ == "__main__":
    meuno = No(2, 3)
    arv = Arvore(meuno)

    print(arv.raiz.valor)
