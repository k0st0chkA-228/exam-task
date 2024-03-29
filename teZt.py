import re


'''На языке Питон написать программу, которая из файла читает объекты, разделенные  пробелами, выводит их на экран,
производит заданную обработку и результат выводит на экран. Обработка: Распознать через регулярные выражения натуральные
четные двоичные числа, в которых вторая и предпоследняя цифра равны 1, из которых определить минимальное число и
 их количество.'''


with open('test.txt', 'r') as f:
    content = f.read()
    pattern = r'\b[0-1][1]*[1][0-1]*[02468]\b'
    numbers = re.findall(pattern, content)
    print(numbers)
    if numbers:
        min_number = min(numbers)
        count = len(numbers)
        print(f"Минимальное число: {min_number}")
        print(f"Количество чисел: {count}")
    else:
        print("Нет подходящих чисел в файле.")
