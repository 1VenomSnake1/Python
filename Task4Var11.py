
'Дана строка в которой записаны слова через пробел.'
'Необходимо упорядочить слова по количеству букв в каждом слове'

def sortlen(str):
    words = str.split(" ")
    words.sort(key=len)
    return words

str = input()
print(sortlen(str))