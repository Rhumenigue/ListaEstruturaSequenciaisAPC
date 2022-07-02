def print_rectangle(x):
    print(x)
    print('+'*x)
    print('+'+' '*(x-2)+'+')
    print('+'*x)
 
    
a,b,c = map(int,input().split())
print_rectangle(a)
print_rectangle(b)
print_rectangle(c)