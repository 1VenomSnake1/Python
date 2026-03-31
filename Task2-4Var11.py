import random


def chaos(str):
    chars = list(str)
    random.shuffle(chars)
    return "".join(chars)

def palindrom(str):
    BigChars = "".join([char for char in str if char.isupper()])

    if not BigChars:
        return False

    return  BigChars == BigChars[::-1]

def sortlen(str):
    words = str.split(" ")
    words.sort(key=len)
    return words


print("Выберите что хотите сделать со строкой: ")
print("1.Перемешать все символы строки в случайном порядке")
print("2.У строки из символов латиницы проверить, образуют ли прописные символы палиндром")
print("3.У строки в которой записаны слова через пробел, упорядочить слова по количеству букв в каждом слове")
choice = int(input())

print("Ваша строка: "
          " ")
if choice == 1:
    str = input()
    print(chaos(str))

if choice == 2:
    str = input()
    if (palindrom(str)):
        print("Да, прописные образуют палиндром")
    else:
        print("Нет, прописные не образуют палиндром")

if choice == 3:
    str = input()
    print(sortlen(str))

elif (choice>3 or choice<1):
    print("Выбрана не существующая опция!")
