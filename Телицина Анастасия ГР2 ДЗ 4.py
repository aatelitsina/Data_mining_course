# 1 (1 балла)
# Напишите функцию calc_factorial, которая вычисляет факториал для любого неотрицательного целого числа.

def calc_factorial(number):
    factorial = 1
    if number > 0:
        for i in range(1, number + 1):
            factorial *= i
    return factorial


# print(calc_factorial(6))

# 2 (1 балл)
# Напишите функцию для нахождения максимума из 3-х аргументов. Не пользуйтесь втроенными функциям Питона
def max_three_arg(a, b, c):
    if a > b and a > c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    return max

# print(max_three_arg(5,10,3))

# 3 балла
# Напишите функцию get_factorial_generator, создающую генератор для вывода последовательности из факториалов целых чисел.
# Дополните уже существующий код:

def get_factorial_generator(numb):
    factorial = 1
    if numb > 0:
        for i in range(1, numb + 1):
            factorial *= i
            yield factorial
        return 'Конец итератора'
factorial_generator = get_factorial_generator(3)
# print(next(factorial_generator))  # печатает 1
# print(next(factorial_generator))  # печатает 2
# print(next(factorial_generator))  # печатает 6
# print(next(factorial_generator))

# 4 (2 + 1 балл)
# 4.1 Используя функцию calc_factorial из первого задания, напишите list comprehension, который из списка чисел получает
#  список факториалов.
# Пример:
# [1, 5, 20, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]
# 4.2 Не изменяя список, модифицируйте list comprehension, чтобы он пропускал числа больше 30: Пример:
# [1, 5, 20, 31, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]

list_number = [1, 5, 20, 31, 3, 7]
# 4.1
print([calc_factorial(x) for x in list_number])
# 4.2
print([calc_factorial(x) for x in list_number if x < 30])

