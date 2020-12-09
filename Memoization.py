from Utilities import *
from DataReader import *
import numpy as np



def start():
    items, capacity = readDataFile("data_4")
    value, taken = memoization(items, capacity)

    print(check_solution(capacity, items, taken), end='')
    print(taken_items(items, taken))


def memoization(items, capacity):
    n = len(items)
    w = capacity
    taken = [0] * len(items)
    mem = np.zeros((n+1, w+1))

    def solved(items, w, n):
        if n == 0 or w == 0:
            return 0
        if mem[n][w] != 0:
            return mem[n][w]

        item = items[n-1]
        if item.weight <= w:
            mem[n][w] = max(item.value + solved(items, w - item.weight, n - 1), solved(items, w, n - 1))
        else:
            mem[n][w] = solved(items, w, n - 1)
        return mem[n][w]

    value = solved(items, w, n)
    i = len(items)
    k = capacity
    while i > 0 and k > 0:
        if mem[i][k] != mem[i-1][k]:
            taken[i-1] = 1
            i -= 1
            k -= items[i].weight
        else:
            i -= 1

    return value, taken



start()
