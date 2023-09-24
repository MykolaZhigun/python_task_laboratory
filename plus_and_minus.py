from random import randint

first_array = []
second_array = []
result_array = []

first_number = ""
second_number = ""
result = ""

number1 = ""
number2 = ""
result_number = ""

def fill_array_with_random_numbers(arr, size):
    for i in range(size):
        arr.append(randint(1, 9))


first_arr_size = int(input("Уведіть розмір першого масива: "))
second_arr_size = int(input("Уведіть розмір другого масива: "))
operation = input("Уведіть операцію + або - : ")

fill_array_with_random_numbers(first_array, first_arr_size)
fill_array_with_random_numbers(second_array, second_arr_size)

len_massiv = len(first_array)
massive_for_reserved = 0

max_size = max(len(first_array), len(second_array))
minus_flag = False
minus_detecter = False

for i in range(max_size - 1, -1, -1):
    while len(first_array) < len(second_array):
        first_array.insert(0, 0)
    while len(second_array) < len(first_array):
        second_array.insert(0, 0)

    if operation == "+":
        add_result = first_array[i] + second_array[i] + massive_for_reserved
        if i == 0:
            result_array.insert(0, add_result)
        else:
            massive_for_reserved = add_result // 10
            result_array.insert(0, add_result % 10)
    elif operation == "-":
        if minus_flag == False:
            for i in range(len(first_array)):
                first_number += str(first_array[i])

            for i in range(len(second_array)):
                second_number += str(second_array[i])


            result = int(first_number) - int(second_number)

            if result < 0:
                minus_detecter = True
                result = abs(result)

            result = str(result)
            for i in result:
                if minus_detecter == True and minus_flag == False:
                    result_array.append("-")
                    minus_flag = True
                result_array.append(i)
            minus_flag = True

print(f"Перший массив: {first_array}")
print(f"Другий массив: {second_array}")
print(f"\nРезультат: {result_array}")
