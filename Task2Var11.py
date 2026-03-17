import random
'''
5. Дана строка. Необходимо перемешать все символы строки в случайном порядке
'''



def chaos(str):
    b = len(str)
    str_copy = str
    while b!=0:
        randomer1 = int(random.randint(0, b))
        randomer2 = int(random.randint(0, b))
        char1 = str[randomer1-1: randomer1]
        char2 = str[randomer2-1:randomer2]
        print(char1 + " "+ char2)
        str_copy.replace
        b-=1
    return


str = input()
print(chaos(str))
