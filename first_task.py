from random import randint

first_array = []
second_array = []
result_array = []

for i in range(10):
    first_array.append(randint(0, 9))
    second_array.append(randint(0, 9))

len_massiv = len(first_array)
massive_for_reserved = 0


for i in reversed(range(len_massiv)):
    add_result = first_array[i] + second_array[i] + massive_for_reserved
    if i == 0:
        result_array.insert(0, add_result)
    else:
        massive_for_reserved = add_result // 10
        result_array.insert(0, add_result % 10)



print(f"Перший массив: {first_array}")
print(f"Другий массив:{second_array}")
print(f"\nРезультат: {result_array}")
