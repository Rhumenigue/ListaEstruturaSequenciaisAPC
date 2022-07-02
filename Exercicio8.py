def trocarAB(x, y):
    print(y, x)
    
for _ in range(5):
    trocarAB(*[int(x) for x in input().split()])