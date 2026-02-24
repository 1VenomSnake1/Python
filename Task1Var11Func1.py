def func1(number):
    p = 1
    kolvo = 0
    while(p<=number):
        if(p % 3 !=0 and number % p ==0):
            kolvo+=1
        p+=1

    return kolvo

number = int(input("Введите число: "))
print("Количество делителей числа: ",number,", не деляющихся на 3 равно: ", func1(number))
