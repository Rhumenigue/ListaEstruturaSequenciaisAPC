def print_rectangle(x):
    print(x)
    print('x'*x)
    for c in range(2):
        print('x'+' '*(x-2)+'x')
    print('x'*x)
 
    
a,b,c = map(int,input().split())
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)