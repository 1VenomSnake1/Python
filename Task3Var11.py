
'Дана строка,, состоящая из символов латиницы.'
'Необходимо проверить, образуют ли прописные символы этой строки палиндром'

def palindrom(str):
    BigChars = "".join([char for char in str if char.isupper()])

    if not BigChars:
        return False

    return  BigChars == BigChars[::-1]


str = input()
if(palindrom(str)):
    print("Да, прописные образуют палиндром")
else:
    print("Нет, прописные не образуют палиндром")