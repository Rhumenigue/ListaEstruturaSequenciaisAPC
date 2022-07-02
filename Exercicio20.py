def pacotesDeBolacha (pacotes, estudantes, maximo):
    while maximo * estudantes > pacotes:
        maximo -= 1
    entrega = maximo*estudantes
    print(entrega)