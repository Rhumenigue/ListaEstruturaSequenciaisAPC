def resto(a,b,d):
    print((a+b)%d)

for c in range(3):
    a,b,d = map(int,input().split())
    resto(a,b,d)