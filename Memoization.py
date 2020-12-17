import sys

sys.setrecursionlimit(999999)


def memoization(items, capacity):
    n = len(items)
    w = capacity
    taken = [0] * len(items)
    mem = {}

    def solved(items, w, n):
        if n == 0 or w == 0:
            return 0

        key = str(str(n) + ": " + str(w))
        if key in mem:
            return mem.get(key)
        else:
            item = items[n-1]
            if item.weight <= w:
                mem[key] = max(item.value + solved(items, w - item.weight, n - 1), solved(items, w, n - 1))
            else:
                mem[key] = solved(items, w, n - 1)
            return mem[key]

    value = solved(items, w, n)
    i = len(items)
    k = capacity
    key1 = str(str(i) + ": " + str(k))
    key2 = str(str(i-1) + ": " + str(k))
    while i > 0 and k > 0:
        if key1 in mem and key2 in mem:
            if mem[key1] != mem[key2]:
                taken[i-1] = 1
                i -= 1
                k -= items[i].weight
            else:
                i -= 1
        else:
            i -= 1
        key1 = str(str(i) + ": " + str(k))
        key2 = str(str(i - 1) + ": " + str(k))

    return value, taken
