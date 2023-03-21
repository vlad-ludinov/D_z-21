from random import randint
lenList = int(input("Введите длину списка: "))
number = int(input("Введите интересующее вас число: "))

numbList = [randint(1,10) for _ in range(lenList)]
count = 0
for i in numbList:
    if i == number:
        count += 1
print(f"Список: {numbList}")
print(f"Введенное число встречается в списке {count} раз")

