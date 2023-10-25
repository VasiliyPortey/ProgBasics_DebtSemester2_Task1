from random import randint

#Студент Портей Василий, сдача задолженности по дисциплине "Основы программирования",
#первый курс, второй семестр, вариант 6, задача первая

def toSet(list1, list2):
    i = 0
    while i<len(list2):
        list1.append(list2[i])
        i+=1
    print("\nКонечный массив с дублями: ", list1)
    return list(set(list1))

length1 = int(input("Введите длину первого массива: "))
list1 = []
for i in range(length1):
    list1.append(randint(-10, 10))
print("\nПервый массив: \n", list1)
length2 = int(input("\nВведите длину второго массива: "))
list2 = []
for i in range(length2):
    list2.append(randint(-10, 10))
print("\nВторой массив: \n", list2)
print("\nКонечный массив без дублей: ", toSet(list1, list2))
    
