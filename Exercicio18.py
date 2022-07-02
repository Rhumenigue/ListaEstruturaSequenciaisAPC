def concatenar(primeiro, segundo):
    print(primeiro+segundo)

def repetir(primeiro, numero):
    print(primeiro*numero)

def ambos(primeiro, segundo, numero):
    print((primeiro+segundo)*numero)

primeiro, segundo, numero = input().split(" ")

numero = int(numero)

concatenar(primeiro, segundo)
repetir(primeiro, numero)
ambos(primeiro, segundo, numero)