import time
from random import random
import numpy as np
from random import randint

class SimulatedAnnealing:
    def __init__(self, queens, n):
        self.queens = queens
        self.n = n
        self.printBoard(self.queens, n)
        start = time.time()
        self.anneal(n)
        end = time.time()

        self.printBoard(self.queens, n)
        print("Runtime", end - start)

    def anneal(self, n):
        currentCost = self.cost(self.queens, n)
        while self.cost(self.queens, n) != 0:

            T = 1.0
            T_min = 0.0001
            alpha = 0.9

            while T>T_min:
                i=1
                if currentCost != 0 and T > T_min:
                    print('working...')
                while (i <= 100):
                    nextState = self.randomNeighbour(self.queens, n)
                    nextCost = self.cost(nextState, n)
                    a = np.exp(-(nextCost - currentCost)/T)

                    if a > random():
                        self.queens = nextState
                        currentCost = nextCost
                        if currentCost == 0:
                            break
                    i += 1

                if currentCost == 0:
                    break
                T = T*alpha

    def randomNeighbour(self, queens, n):

        queensTemp = queens[:]

        i = randint(0, n-1)
        j = randint(0, n-1)

        queensTemp[i]=j
       # print("queensTemp: ",queensTemp)
       # queensCost = self.cost(queensTemp, n)
       # print("queensCost:", queensCost)
        return queensTemp[:]

    def cost(self, queens, n):
        conflict = 0
        for i in range(n):
            for j in range(i + 1, n):
                if i != j:
                    if queens[i] == queens[j]:
                        conflict = conflict + 1
                    if abs(queens[i] - queens[j]) == abs(i-j):
                        conflict = conflict + 1
        return int(conflict)
    def printBoard(self ,queens, n):
        print("\n")
        for i in range(n):
            print("|", end='\t')
            for j in range(n):
                if queens[j] == i:
                    print("x|", end='\t')
                else:
                    print(" |", end='\t')
            print("\n")
        currentCost = self.cost(self.queens, n)
        print('\r', "cost:", currentCost, self.queens, end='\n', flush=True)

n = 8
queens = list((randint(0, n - 1) for x in range(n)))
result = SimulatedAnnealing(queens, n)
