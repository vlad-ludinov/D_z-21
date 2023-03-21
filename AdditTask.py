from random import randint
k1 = int(input("Введите первую степень: "))
k2 = int(input("Введите вторую степень: "))



polycan1 = ""
flag1 = False
coefficients = [randint(0,10) for _ in range(k1+1)]


for i in range(2, k1+1):
    j = i - 1
    while coefficients[j] == 0 and j < k1:
        if coefficients[j+1] != 0:
            flag1 = False
        j +=1 
    if flag1:
        if coefficients[i-2] != 0:
            polycan1 += str(coefficients[i-2])
            polycan1 += "x^"
            polycan1 += str(k1 - (i-2))
    else:
        if coefficients[i-2] != 0:  
            polycan1 += str(coefficients[i-2])
            polycan1 += "x^"
            polycan1 += str(k1 - (i-2))
            polycan1 += " + "
    if coefficients[i] == 0:
        flag1 = True

if flag1 == False:
    if coefficients[k1-1] != 0:
        polycan1 += str(coefficients[k1-1])
        polycan1 += "x"
        polycan1 += " + "
        polycan1 += str(coefficients[k1])
    else:
        polycan1 += str(coefficients[k1])
else:
    if coefficients[k1-1] != 0:
        polycan1 += str(coefficients[k1-1])
        polycan1 += "x"


polycan2 = ""
flag2 = False
coefficients = [randint(0,10) for _ in range(k2+1)]
for i in range(2, k2+1):
    j = i - 1
    while coefficients[j] == 0 and j < k2:
        if coefficients[j+1] != 0:
            flag2 = False
        j +=1 
    if flag2:
        if coefficients[i-2] != 0:
            polycan2 += str(coefficients[i-2])
            polycan2 += "x^"
            polycan2 += str(k2 - (i-2))
    else:
        if coefficients[i-2] != 0:  
            polycan2 += str(coefficients[i-2])
            polycan2 += "x^"
            polycan2 += str(k2 - (i-2))
            polycan2 += " + "
    if coefficients[i] == 0:
        flag2 = True

if flag2 == False:
    if coefficients[k2-1] != 0:
        polycan2 += str(coefficients[k2-1])
        polycan2 += "x"
        polycan2 += " + "
        polycan2 += str(coefficients[k2])
    else:
        polycan2 += str(coefficients[k2])
else:
    if coefficients[k2-1] != 0:
        polycan2 += str(coefficients[k2-1])
        polycan2 += "x"


print("Получаются следующие многочлены:")

splitPolycan1 = polycan1.split(" + ")
splitPolycan2 = polycan2.split(" + ")


dictPolycan1 = {}
dictPolycan2 = {}

for i in splitPolycan1:
    temp = i.split("x^")
    if i == temp[0]:
        temp = i.split("x")
        if i == temp[0]:
            dictPolycan1[0] = int(temp[0])
        else:
            dictPolycan1[1] = int(temp[0])
    else:
        dictPolycan1[int(temp[1])] = int(temp[0])

for i in splitPolycan2:
    temp = i.split("x^")
    if i == temp[0]:
        temp = i.split("x")
        if i == temp[0]:
            dictPolycan2[0] = int(i)
        else:
            dictPolycan2[1] = int(temp[0])
    else:
        dictPolycan2[int(temp[1])] = int(temp[0])


if k1<k2:
    kmax = k2
else:
    kmax = k1
kmaxtemp = kmax

finalPolycan = {}
for i in range(kmaxtemp+1):
    if dictPolycan1.get(kmaxtemp) != None and dictPolycan2.get(kmaxtemp) != None:
        finalPolycan[kmaxtemp] = dictPolycan1.get(kmaxtemp) + dictPolycan2.get(kmaxtemp) 
    elif dictPolycan1.get(kmaxtemp) != None:
        finalPolycan[kmaxtemp] = dictPolycan1.get(kmaxtemp)
    elif dictPolycan2.get(kmaxtemp) != None:
        finalPolycan[kmaxtemp] = dictPolycan2.get(kmaxtemp)
    kmaxtemp-=1


answer = ""
flag = False
for i in range(kmax, -1, -1):
    j = i-1
    while finalPolycan.get(j) == None and j > -1:
        if finalPolycan.get(j-1) != None:
            flag = False
        j -= 1
    if finalPolycan.get(i) != None:
        if flag:
            if i >1:
                answer += str(finalPolycan.get(i))
                answer += "x^"
                answer += str(i)
            elif i == 1:
                answer += str(finalPolycan.get(i))
                answer += "x"
            else:
                answer += str(finalPolycan.get(i))
        else:
            if i >1:
                answer += str(finalPolycan.get(i))
                answer += "x^"
                answer += str(i)
                answer += " + "
            elif i == 1:
                answer += str(finalPolycan.get(i))
                answer += "x"
                answer += " + "
            else:
                answer += str(finalPolycan.get(i))
    if finalPolycan.get(i-2) == None:
        flag = True
print("При сложении этих двух многочленов получается")
print(answer)