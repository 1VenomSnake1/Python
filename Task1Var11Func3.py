import math

def func3(number):
    temp = number
    summa = 0
    proiz = 1
    otvet = 0
    while(temp!=0):
        summa+=temp%10
        proiz *= temp % 10
        temp//=10
    print(summa)
    print(proiz)
    temp = 1
    while temp <= number:
        if number % temp == 0 and math.gcd(temp, summa) == 1 and math.gcd(temp, proiz) != 1:
            otvet+=temp
            print(otvet, " ", temp)
        temp+=1
    return otvet

number = int(input("Введите число: "))
print("Сумма всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа: ", func3(number))