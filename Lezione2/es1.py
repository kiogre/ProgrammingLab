def sum_list(lista):
    if lista == []:
        return None
    tot = 0
    for i in lista:
        tot = tot + i
    return tot