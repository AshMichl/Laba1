from math import factorial as fact

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
factrion = []

print('4х-значные числа, равные сумме факториалов своих цифр входящие в диапазон')
for i in range(a, b):
    if len(str(i)) >= 7:
        print("ghghfghdrg")
        print(i)
        print(len(str(i)))
        break
    else:
        s = sum([fact(int(x)) for x in str(i)])
        if s == i:
            print(i)
            factrion.append(i)

if len(factrion) == 0:
    print('Таких чисел нет')
