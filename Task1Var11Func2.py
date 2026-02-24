def func2(number):
    temp = number
    min = 9
    while (temp!=0):
        if((temp%10)%2!=0 and temp%10<min):
            min = temp%10
        temp//=10
    return min

number = int(input("Введите число: "))
print("Минимальная нечётная цифра числа: ",number," равна: ", func2(number))
