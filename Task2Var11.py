import random
'''
5. Дана строка. Необходимо перемешать все символы строки в случайном порядке
'''



def chaos(str):
    chars = list(str)
    random.shuffle(chars)
    return "".join(chars)


str = input()
print(chaos(str))
