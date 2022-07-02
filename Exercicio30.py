data = str(input())
DD, MM, AA = data[0:2], data[3:5], data[6:8]

print(f'{DD}-{MM}-{AA}')
print(f'{MM}-{DD}-{AA}')
print(f'{AA}/{MM}/{DD}')