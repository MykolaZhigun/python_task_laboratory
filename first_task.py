from random import randint

first_array = []
second_array = []
result_array = []

for i in range(10):
    first_array.append(randint(0, 9))
    second_array.append(randint(0, 9))

massive_for_reserved = 0
for i in range(9, -1, -1):
    add_result = first_array[i] + second_array[i] + massive_for_reserved
    massive_for_reserved = add_result // 10
    result_array.insert(0, add_result % 10)

if massive_for_reserved > 0:
    result_array.insert(0, massive_for_reserved)

# Вывод массивов и суммы в столбик
print(f"Первый массив: {first_array}")
print(f"Второй массив:{second_array}")
print(f"Результат: {result_array}")
