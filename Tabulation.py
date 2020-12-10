import numpy as np


def fillTable(table, items, capacity):
    for i in range(1, len(items)+1):
        for w in range(capacity+1):
            if items[i-1].weight <= w:
                if items[i-1].value + table[i-1][w-items[i-1].weight] > table[i-1][w]:
                    table[i][w] = items[i-1].value + table[i-1][w-items[i-1].weight]
                else:
                    table[i][w] = table[i-1][w]
            else:
                table[i][w] = table[i-1][w]
    return table


def tabulation(items, capacity):
    i = len(items)
    k = capacity

    taken = [0] * len(items)
    table = np.zeros((len(items)+1, capacity+1))
    table = fillTable(table, items, capacity)

    while i > 0 and k > 0:
        if table[i][k] != table[i-1][k]:
            taken[i-1] = 1
            i -= 1
            k -= items[i].weight
        else:
            i -= 1

    return table[len(items)-1][capacity], taken
