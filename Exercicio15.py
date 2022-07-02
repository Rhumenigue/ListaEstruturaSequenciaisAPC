def qualPeriodo(semestre, ano, digito):
    total = 2*(ano - int('20'+str(semestre)[:2]))
    print(total-int(str(semestre)[3])+digito+1)