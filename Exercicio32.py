n1, n2, n3 = map(float, input().split())

p1, p2, p3 = map(float, input().split())

media = float(((n1*p1)+(n2*p2)+(n3*p3))/(p1+p2+p3))

print(f'{media:.6f}')

