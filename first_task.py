from random import randint

first_massiv = []
second_massiv = []
result_massiv = []

for i in range(10):
    first_massiv.append(randint(0,9))
    second_massiv.append(randint(0, 9))

for i in range(10):
    result_massiv.append(first_massiv[i] + second_massiv[i])

print(f"Перший масив: {first_massiv}")
print(f"Другий масив: {second_massiv}")
print(f"Результат: {result_massiv[::-1]}")
