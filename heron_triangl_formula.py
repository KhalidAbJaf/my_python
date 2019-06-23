import math

msg = 'Вычитываем площадь треугольника по формуле Герона'

a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

p = (a + b + c) / 2

S = math.sqrt(p*(p-a)*(p-b)*(p-c))

print('Площадь треугольника = ', S)