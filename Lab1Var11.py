import random
import re
import math
from collections import Counter

# Задание 1. Функции для работы с цифрами и делителями (вариант 11)
def count_divisors_not_divisible_by_3(n: int) -> int:
    """Функция 1. Количество делителей числа, не делящихся на 3."""
    if n == 0:
        return 0
    count = 0
    for i in range(1, int(abs(n)) + 1):
        if n % i == 0 and i % 3 != 0:
            count += 1
    return count

def min_odd_digit(n: int) -> int:
    """Функция 2. Минимальная нечётная цифра числа. Если нет – вернёт -1."""
    digits = [int(d) for d in str(abs(n))]
    odd_digits = [d for d in digits if d % 2 == 1]
    return min(odd_digits) if odd_digits else -1

def sum_divisors_coprime_with_sum_and_not_coprime_with_prod(n: int) -> int:
    """
    Функция 3. Сумма делителей числа, которые:
      - взаимно просты с суммой цифр числа,
      - не взаимно просты с произведением цифр числа.
    """
    if n == 0:
        return 0
    n_abs = abs(n)
    # сумма цифр
    digit_sum = sum(int(d) for d in str(n_abs))
    # произведение цифр (если есть 0, произведение = 0, тогда НОД(делитель,0)=|делитель| >1 для любого |делитель|>1)
    prod = 1
    for d in str(n_abs):
        prod *= int(d)
    # все делители
    divisors = [i for i in range(1, n_abs + 1) if n_abs % i == 0]
    total = 0
    for d in divisors:
        if math.gcd(d, digit_sum) == 1 and math.gcd(d, prod) > 1:
            total += d
    return total

# Задания 2-4. Задачи 5, 7, 14
def task_shuffle_string(s: str) -> str:
    """Перемешать все символы строки в случайном порядке."""
    lst = list(s)
    random.shuffle(lst)
    return ''.join(lst)

def task_uppercase_palindrome(s: str) -> bool:
    """Проверить, образуют ли прописные символы латиницы палиндром."""
    uppercase = [ch for ch in s if ch.isupper() and ch.isalpha() and 'A' <= ch <= 'Z']
    return uppercase == uppercase[::-1]

def task_sort_words_by_length(s: str) -> str:
    """Упорядочить слова по количеству букв (по возрастанию)."""
    words = s.split()
    words.sort(key=len)
    return ' '.join(words)

def menu_tasks_2_4():
    print("\n--- Задания 2-4 ---")
    print("1. Перемешать все символы строки")
    print("2. Проверить палиндром из прописных латинских букв")
    print("3. Упорядочить слова по длине")
    choice = input("Выберите задачу (1-3): ")
    s = input("Введите строку: ")
    if choice == '1':
        print("Результат:", task_shuffle_string(s))
    elif choice == '2':
        print("Результат:", task_uppercase_palindrome(s))
    elif choice == '3':
        print("Результат:", task_sort_words_by_length(s))
    else:
        print("Неверный выбор.")

# Задание 5. Найти все даты вида "31 февраля 2007"
def find_fake_dates(text: str) -> list:
    """Находит все вхождения дат '31 февраля 2007'."""
    pattern = r'31 февраля 2007'
    return re.findall(pattern, text)

def task5():
    print("\n--- Задание 5: поиск дат '31 февраля 2007' ---")
    text = input("Введите строку: ")
    dates = find_fake_dates(text)
    if dates:
        print("Найдены даты:", dates)
    else:
        print("Даты не найдены.")

# Задания 6-8. Задачи 5, 7, 14
def max_consecutive_cyrillic(s: str) -> int:
    """Наибольшее количество идущих подряд символов кириллицы."""
    # Диапазоны кириллицы: А-Я, а-я, Ё, ё
    pattern = r'[А-Яа-яЁё]+'
    matches = re.findall(pattern, s)
    if not matches:
        return 0
    return max(len(m) for m in matches)

def min_natural_number(s: str) -> int:
    """Минимальное натуральное число в строке (целое положительное)."""
    numbers = re.findall(r'\b[1-9][0-9]*\b', s)
    if not numbers:
        return None
    return min(int(num) for num in numbers)

def max_consecutive_digits(s: str) -> int:
    """Наибольшее количество идущих подряд цифр."""
    matches = re.findall(r'\d+', s)
    if not matches:
        return 0
    return max(len(m) for m in matches)

def menu_tasks_6_8():
    print("\n--- Задания 6-8 ---")
    print("1. Наибольшее количество подряд символов кириллицы")
    print("2. Минимальное натуральное число в строке")
    print("3. Наибольшее количество подряд цифр")
    choice = input("Выберите задачу (1-3): ")
    s = input("Введите строку: ")
    if choice == '1':
        print("Результат:", max_consecutive_cyrillic(s))
    elif choice == '2':
        res = min_natural_number(s)
        print("Результат:", res if res is not None else "Натуральных чисел не найдено")
    elif choice == '3':
        print("Результат:", max_consecutive_digits(s))
    else:
        print("Неверный выбор.")

# Задание 9. Упорядочить список строк по длине
def task9():
    print("\n--- Задание 9: сортировка строк по длине ---")
    lines = []
    print("Введите строки (пустая строка – конец ввода):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    lines.sort(key=len)
    print("Отсортированный список:")
    for line in lines:
        print(line)

# Задание 10. Упорядочить список строк по количеству слов
def task10():
    print("\n--- Задание 10: сортировка строк по количеству слов ---")
    lines = []
    print("Введите строки (пустая строка – конец ввода):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    lines.sort(key=lambda x: len(x.split()))
    print("Отсортированный список:")
    for line in lines:
        print(line)

# Задания 11-14. Задачи 2, 6, 9, 12
def ascii_mean(s: str) -> float:
    """Средний вес ASCII-кода символов строки."""
    if not s:
        return 0.0
    return sum(ord(ch) for ch in s) / len(s)

def median_ascii(s: str) -> float:
    """Медиана ASCII-кодов символов строки."""
    if not s:
        return 0.0
    codes = sorted(ord(ch) for ch in s)
    n = len(codes)
    if n % 2 == 1:
        return codes[n // 2]
    else:
        return (codes[n // 2 - 1] + codes[n // 2]) / 2

def deviation_max_ascii_and_mirror_diffs(s: str) -> float:
    """
    Квадратичное отклонение между наибольшим ASCII-кодом строки
    и разницами зеркальных пар символов (стандартное отклонение).
    """
    if not s:
        return 0.0
    codes = [ord(ch) for ch in s]
    max_code = max(codes)
    n = len(codes)
    diffs = []
    for i in range(n // 2):
        diff = abs(codes[i] - codes[n - 1 - i])
        diffs.append(diff)
    if not diffs:
        return 0.0
    # Среднее квадратичное отклонение разностей от max_code
    mean_diff = sum(diffs) / len(diffs)
    variance = sum((d - max_code) ** 2 for d in diffs) / len(diffs)
    return math.sqrt(variance)

def global_freq_deviation(strings: list, global_char: str, global_freq: float, s: str) -> float:
    """
    Квадрат разности между глобальной частотой символа global_char
    и его частотой в строке s.
    """
    if not s:
        return global_freq ** 2   # частота в пустой строке = 0
    count_in_s = s.count(global_char)
    freq_in_s = count_in_s / len(s)
    return (global_freq - freq_in_s) ** 2

def menu_tasks_11_14():
    print("\n--- Задания 11-14 ---")
    print("Выберите критерий сортировки:")
    print("1. По среднему весу ASCII-кода")
    print("2. По медиане ASCII-кодов")
    print("3. По квадратичному отклонению (max_ascii vs зеркальные разности)")
    print("4. По квадратичному отклонению частоты самого частого символа в наборе")
    choice = input("Ваш выбор: ")

    # Ввод списка строк
    lines = []
    print("Введите строки (пустая строка – конец ввода):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    if not lines:
        print("Нет данных.")
        return

    if choice == '1':
        lines.sort(key=ascii_mean)
        print("Отсортировано по среднему весу ASCII:")
        for line in lines:
            print(line)
    elif choice == '2':
        lines.sort(key=median_ascii)
        print("Отсортировано по медиане ASCII-кодов:")
        for line in lines:
            print(line)
    elif choice == '3':
        lines.sort(key=deviation_max_ascii_and_mirror_diffs)
        print("Отсортировано по квадратичному отклонению (max_ascii / зерк. разности):")
        for line in lines:
            print(line)
    elif choice == '4':
        # Находим самый частотный символ во всём наборе строк
        all_text = ''.join(lines)
        if not all_text:
            print("Все строки пусты.")
            return
        char_counts = Counter(all_text)
        most_common_char, global_count = char_counts.most_common(1)[0]
        global_freq = global_count / len(all_text)
        # Сортируем строки по квадрату разности частот
        lines.sort(key=lambda s: (global_freq - (s.count(most_common_char)/len(s) if s else 0)) ** 2)
        print(f"Отсортировано по квадратичному отклонению частоты символа '{most_common_char}':")
        for line in lines:
            print(line)
    else:
        print("Неверный выбор.")

# Задания 15-19. Задачи 11,23,35,47,59
def find_unique_element(arr):
    """Задача 11. Элемент, отличающийся от остальных."""
    if not arr:
        return None
    count = Counter(arr)
    for val, cnt in count.items():
        if cnt == 1:
            return val
    return None

def two_smallest(arr):
    """Задача 23. Два наименьших элемента."""
    if len(arr) < 2:
        return sorted(arr)[:len(arr)]
    # Находим два наименьших без полной сортировки
    smallest = [float('inf'), float('inf')]
    for x in arr:
        if x < smallest[0]:
            smallest[1] = smallest[0]
            smallest[0] = x
        elif x < smallest[1]:
            smallest[1] = x
    return smallest

def closest_element(R, arr):
    """Задача 35. Элемент, наиболее близкий к R."""
    if not arr:
        return None
    return min(arr, key=lambda x: abs(x - R))

def all_positive_divisors_of_list(lst):
    """Задача 47. Список всех положительных делителей элементов списка без повторений."""
    divisors = set()
    for num in lst:
        if num <= 0:
            continue
        num = abs(num)
        for i in range(1, int(math.isqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
    return sorted(divisors)

def squares_of_frequent_numbers(lst):
    """Задача 59. Квадраты чисел (x^2) для x >=0, x<100, встречающихся >2 раз."""
    counter = Counter(lst)
    result = []
    for x, cnt in counter.items():
        if isinstance(x, (int, float)) and 0 <= x < 100 and cnt > 2:
            result.append(x * x)
    return sorted(result)

def menu_tasks_15_19():
    print("\n--- Задания 15-19 ---")
    print("1. Элемент, отличающийся от остальных")
    print("2. Два наименьших элемента")
    print("3. Ближайший элемент к заданному числу")
    print("4. Все положительные делители элементов списка")
    print("5. Квадраты чисел, встречающихся >2 раз (0<=x<100)")
    choice = input("Выберите задачу: ")

    if choice == '1':
        arr = list(map(int, input("Введите целые числа через пробел: ").split()))
        print("Уникальный элемент:", find_unique_element(arr))
    elif choice == '2':
        arr = list(map(int, input("Введите целые числа через пробел: ").split()))
        print("Два наименьших:", two_smallest(arr))
    elif choice == '3':
        R = float(input("Введите число R: "))
        arr = list(map(float, input("Введите вещественные числа через пробел: ").split()))
        print("Ближайший элемент:", closest_element(R, arr))
    elif choice == '4':
        arr = list(map(int, input("Введите положительные числа через пробел: ").split()))
        print("Все положительные делители:", all_positive_divisors_of_list(arr))
    elif choice == '5':
        arr = list(map(int, input("Введите числа через пробел: ").split()))
        print("Квадраты чисел (>=0,<100, >2 раз):", squares_of_frequent_numbers(arr))
    else:
        print("Неверный выбор.")

# Главное меню
def main():
    while True:
        print("\n" + "="*50)
        print("1. Задание 1 (три функции)")
        print("2. Задания 2-4 (строки, задачи 5,7,14)")
        print("3. Задание 5 (поиск дат '31 февраля ГГГГ')")
        print("4. Задания 6-8 (строки, задачи 5,7,14)")
        print("5. Задание 9 (сортировка строк по длине)")
        print("6. Задание 10 (сортировка строк по числу слов)")
        print("7. Задания 11-14 (сложная сортировка строк)")
        print("8. Задания 15-19 (списки, задачи 11,23,35,47,59)")
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == '1':
            n = int(input("Введите целое число: "))
            print(f"Количество делителей, не делящихся на 3: {count_divisors_not_divisible_by_3(n)}")
            print(f"Минимальная нечётная цифра: {min_odd_digit(n)}")
            print(f"Сумма делителей по условию: {sum_divisors_coprime_with_sum_and_not_coprime_with_prod(n)}")
        elif choice == '2':
            menu_tasks_2_4()
        elif choice == '3':
            task5()
        elif choice == '4':
            menu_tasks_6_8()
        elif choice == '5':
            task9()
        elif choice == '6':
            task10()
        elif choice == '7':
            menu_tasks_11_14()
        elif choice == '8':
            menu_tasks_15_19()
        elif choice == '0':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()