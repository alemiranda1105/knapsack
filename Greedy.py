import random
from collections import namedtuple


# Tupla auxiliar don de guardamos el ratio value/weight
Ratio = namedtuple("Ratio", ['index', 'vw'])


def quickSort(items, inDesiredOrder):

    def partitionrand(arr, start, stop, order):
        randpivot = random.randrange(start, stop)

        arr[start], arr[randpivot] = arr[randpivot], arr[start]
        return partition(arr, start, stop, order)

    def partition(arr, start, stop, order):
        pivot = start

        i = start + 1

        for j in range(start + 1, stop + 1):

            if order(arr[j], arr[pivot]):
                arr[i], arr[j] = arr[j], arr[i]
                i = i + 1

        arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
        pivot = i - 1
        return pivot

    def qs(arr, start, stop, order):
        if start < stop:
            pivotindex = partitionrand(arr, start, stop, order)

            qs(arr, start, pivotindex - 1, order)
            qs(arr, pivotindex + 1, stop, order)

    qs(items, 0, len(items) - 1, inDesiredOrder)


# Buscamos los elementos con mejor ratio de valor/peso y los metemos en la mochila
def solve_greedy(items, capacity):
    quickSort(items, lambda x, y: x.value > y.value)

    value = 0
    weight = 0
    taken = [0] * len(items)
    rat = []

    # Calculo del ratio value/weight
    for item in items:
        rat.append(Ratio(item.index, item.value/item.weight))

    quickSort(rat, lambda x, y: x.vw > y.vw)
    for r in rat:
        item = items[r.index]
        if item.weight + weight <= capacity:
            taken[item.index] = 1
            weight += item.weight
            value += item.value

    return value, taken
