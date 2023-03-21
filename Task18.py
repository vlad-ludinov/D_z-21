from random import randint
lenList = int(input("Введите длину списка: "))
number = int(input("Введите интересующее вас число: "))

numbList = [randint(1,10) for _ in range(lenList)]
indexRequiredNumber = []
differenceNumbers = []
for i in numbList:
    differenceNumbers.append(abs(i-number))
minNumber = 1000000000
for i in range(len(differenceNumbers)):
    if differenceNumbers[i] < minNumber:
        minNumber = differenceNumbers[i]
        indexRequiredNumber.clear()
        indexRequiredNumber.append(i)
    elif differenceNumbers[i] == minNumber:
        indexRequiredNumber.append(i)
print(f"Список: {numbList}")
print(f"Самое близкое число к заданному числу это число {numbList[indexRequiredNumber[0]]}")
if len(indexRequiredNumber)>1:

    print(f"Это число встречается в списке {len(indexRequiredNumber)} раз и находится под индексами: {indexRequiredNumber}")
else:
    print(f"Это число встречается в списке {len(indexRequiredNumber)} раз и находится под индексом: {indexRequiredNumber}")

