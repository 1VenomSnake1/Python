'''
1 Функция Найти количество делителей числа, не деляющихся на 3
2 Функция найти минимальную нечётную цифру числа
3 Функция Найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа
'''
from ftplib import parse150
from sys import flags
import math

def func1(number):
    p = 1
    kolvo = 0
    while(p<=number):
        if(p % 3 !=0 and number % p ==0):
            kolvo+=1
        p+=1

    return kolvo

def func2(number):
    temp = number
    min = 9
    while (temp!=0):
        if((temp%10)%2!=0 and temp%10<min):
            min = temp%10
        temp//=10
    return min

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
print("Количество делителей числа: ",number,", не деляющихся на 3 равно: ", func1(number))
print("Минимальная нечётная цифра числа: ",number," равна: ", func2(number))
print("Сумма всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых с произведением цифр числа: ", func3(number))