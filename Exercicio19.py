def pacotesDeBolacha (pacotes, estudantes, maximo):
    while maximo * estudantes > pacotes:
        maximo -= 1
    resto = pacotes - (estudantes * maximo)
    print(resto)