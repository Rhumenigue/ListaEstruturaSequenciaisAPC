import math

def powAPC({x},{y}):


  x, y = input().split()
  print(f'powAPC ({x}, {y})')
  x = float(x)
  y = float(y)

  print(math.pow(x,y))


powAPC()
