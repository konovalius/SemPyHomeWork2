# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
n = int(input('Введите n:'))
count = 0
for _ in range(n):
    coins = random.randint(0, 1)
    print(coins)
    if coins == 0:
        count = count+1

print('нужно перевернуть ', count, 'монеты')