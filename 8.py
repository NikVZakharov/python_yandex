numbers = [2, 5, 7, 7, 8, 4, 1, 6]  # список чисел
odd = []  # список нечётных чисел
even = []   # список чётных чисел
for number in numbers:
    if number % 2 == 0:  # проверка на чётность
        even.append(number)  # добавление в список чётных чисел
    else:
        odd.append(number)    # добавление в список нечётных чисел
