# -*- coding: utf-8 -*-

#DANIEL MORAIS - CONTROLE INTELIGENTE - ENG. COMPUTAÇÃO - UFRN 2018.1

class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        #return "".join(["x = ", str(self.x), ", y = ", str(self.y)])
        return "".join([str(self.x)," ",str(self.y)])
