def age(x):
    years, rest = divmod(x,360)
    months, days = divmod(rest,30)
    print (f'{years} {months} {days}')

for x in [int (y) for y in input().split()]:
    age(x)