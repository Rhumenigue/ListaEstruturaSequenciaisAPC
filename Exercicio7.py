def maiorAB(x, y):
    print(max([x, y]))
    
for _ in range(5):
    maiorAB(*[int(x) for x in input().split()])