hora = str(input())

h, m, s = int(hora[0:2]), int(hora[3:5]), int(hora[6:8])
hes = h*3600
mes = m*60
stotal = hes + mes + s
print(f'La se foram {stotal} segundos que nao voltam mais...')