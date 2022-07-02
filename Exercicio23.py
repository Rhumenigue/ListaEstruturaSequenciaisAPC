def ritmoMedio(a, b, c, d):
    horasEmSegundos = a*3600
    minutosEmSegundos = b*60
    segundosTotais = horasEmSegundos + minutosEmSegundos + c
    segundosPorKm = segundosTotais /d
    minutos = segundosPorKm // 60
    segundos = segundosPorKm % 60
    minutos, segundos = [int(i) for i in [minutos, segundos]]
    if minutos < 10:
        minutos = f'0{minutos}'
    if segundos < 10:
        segundos = f'0{segundos}'
    print(f'{minutos}:{segundos} min/km')
        