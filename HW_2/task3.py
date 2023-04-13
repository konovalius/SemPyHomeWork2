"""Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N."""

n = int(input('Введите число N:'))
value=2
for _ in range(n+1):
    if value <= n:
        print(value)
        value=value+2
    else:
        break