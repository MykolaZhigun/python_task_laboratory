from random import randint

first_array = []
second_array = []
result_array = []

def fill_array_with_random_numbers(arr, size):
    for i in range(size):
        arr.append(randint(1, 9))

first_arr_size = int(input("Уведіть розмір першого масива: "))
second_arr_size = int(input("Уведіть розмір другого масива: "))

fill_array_with_random_numbers(first_array, first_arr_size)
fill_array_with_random_numbers(second_array, second_arr_size)


len_massiv = len(first_array)
massive_for_reserved = 0

max_size = max(len(first_array), len(second_array))

for i in range(max_size - 1, -1, -1):
    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)

    add_result = first_array[i] + second_array[i] + massive_for_reserved
    if i == 0:
        result_array.insert(0, add_result)
    else:
        massive_for_reserved = add_result // 10
        result_array.insert(0, add_result % 10)



print(f"Перший массив: {first_array}")
print(f"Другий массив:{second_array}")
print(f"\nРезультат: {result_array}")
