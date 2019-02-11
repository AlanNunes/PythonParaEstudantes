lst = [[10, 12, 13], [10, [26, 30, [27, 18, 19]]]]

def somaValores(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += somaValores(i)
        else:
            total += i
    return total

print(somaValores(lst))
