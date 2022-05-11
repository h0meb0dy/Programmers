a, b = map(int, input().strip().split(' '))
rectangle = ''

for row in range(b):
    for col in range(a):
        rectangle += '*'
    rectangle += '\n'

print(rectangle)