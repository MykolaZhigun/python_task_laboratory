class Human():
    def __init__(self, name, year, height, weight, country):
        self.name_human = name
        self.year_human = year
        self.height_human = height
        self.weight_human = weight
        self.country_human = country

class HumanInformation(Human):
    def country_information(self):
        print(f"{self.name_human} з {self.country_human}")

first_human = HumanInformation("Володимир", "17", "178", "61", "України")
second_human = HumanInformation("Сергій", "26", "194", "82", "Польщі")

#Вивід данних
print("\n\nВивід данних про першу людину:")
print(f"Ім'я: {first_human.name_human}")
print(f"Кількість років: {first_human.year_human}")
print(f"Зріст: {first_human.height_human}")
print(f"Вага: {first_human.weight_human}")
print(first_human.country_information())


print("\nВивід данних про другу людину:")
print(f"Ім'я: {second_human.name_human}")
print(f"Кількість років: {second_human.year_human}")
print(f"Зріст: {second_human.height_human}")
print(f"Вага: {second_human.weight_human}")
print(second_human.country_information())
