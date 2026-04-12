import re

text = (str(input()))

pattern = r"\d{1,2}\s+[а-яА-Я]+\s+\d{4}"

dates = re.findall(pattern, text)
print(dates)