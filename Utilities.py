from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])


# Valor de la mochila en total
def get_total_value(items, taken):
    value = 0
    for item in items:
        if taken[item.index] == 1:
            value += item.value

    return value


# Peso total de los elementos escogidos
def get_total_weight(items, taken):
    weight = 0
    for item in items:
        if taken[item.index] == 1:
            weight += item.weight

    return weight


# Peso restante en la mochila
def get_left_weight(capacity, items, taken):
    return capacity - get_total_weight(items, taken)


# Comprobación de la solución
def check_solution(capacity, items, taken):
    weight = get_total_weight(items, taken)
    value = get_total_value(items, taken)
    if weight > capacity:
        print("Solución incorrecta, se supera la capacidad de la mochila (capacity, weight):", capacity, weight)
        return 0
    return value


# Devuelve el index de los elementos escogidos
def taken_items(items, taken):
    def get_taken_list(taken):
        result = []
        for j in range(0, len(taken)):
            if taken[j]: result.append(j)
        return result

    items.sort(key=lambda x: getattr(x, 'index'), reverse=False)
    return get_taken_list(taken)
