def peso_ideal(altura):
    homem_peso = round((72.7 * altura) - 58, 2)
    mulher_peso = round((62.1 * altura) - 44.7, 2)
    print(f'{homem_peso:.2f} {mulher_peso:.2f}')


peso_ideal(float(input()))
