def vestimentas(x,y):
    numerosPares = 0
    if x > y:
        numerosPares = x - (x-y)
    else:
        numerosPares = y - (y-x)
    print(numerosPares)