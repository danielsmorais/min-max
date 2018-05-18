from point import Point
from no import No
from tabuleiro import Tabuleiro as Tab
from arvore import Arvore as Arv
import copy
from math import inf


def alinhamento(tab, player):
    
    #adiciona o seu valor às celulas vazias
    for item in tab.getNone():              # lista de None points
        tab.setLocal(item, player)

    #verificar alinhamentos
    vencer = [[tab.getLocal(Point(0, 0)), tab.getLocal(Point(0, 1)), tab.getLocal(Point(0, 2))],
              [tab.getLocal(Point(1, 0)), tab.getLocal(
                  Point(1, 1)), tab.getLocal(Point(1, 2))],
              [tab.getLocal(Point(2, 0)), tab.getLocal(
                  Point(2, 1)), tab.getLocal(Point(2, 2))],

              [tab.getLocal(Point(0, 0)), tab.getLocal(
                  Point(1, 0)), tab.getLocal(Point(2, 0))],
              [tab.getLocal(Point(0, 1)), tab.getLocal(
                  Point(1, 1)), tab.getLocal(Point(2, 1))],
              [tab.getLocal(Point(0, 2)), tab.getLocal(
                  Point(1, 2)), tab.getLocal(Point(2, 2))],

              [tab.getLocal(Point(0, 0)), tab.getLocal(
                  Point(1, 1)), tab.getLocal(Point(2, 2))],
              [tab.getLocal(Point(2, 0)), tab.getLocal(Point(1, 1)), tab.getLocal(Point(0, 2))]]

    alinhamento = 0

    for indice, valor in enumerate(vencer):
        if [player, player, player] == valor:
            alinhamento += player

    print(alinhamento)

    return alinhamento


def heuri(tab,player):

    score = alinhamento(copy.deepcopy(tab), player)
    tab.show()

    print(score)

    score1 = alinhamento(copy.deepcopy(tab), -player)
    
    print(score1)

    return score


    
    

def minimax(tab, prof, player):
    
    best = []

    for item in tab.getNone():  # lista de None points
        tab.setLocal(item, player)

        score = minimax(tab, prof - 1, -player)
        tab.setLocal(item, None)
        score[0], score[1] = item.x, item.y

        if player == 1:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best  # retorna x y score

if __name__ == "__main__":

    tab = Tab([[None, None, None], [None, None, None], [None, None, None]])
    
    #minimax(tab,9,1)
    heuri(tab,1)

