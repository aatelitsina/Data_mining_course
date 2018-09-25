# 1. (3 балла)
# Напишите программу, в которой пользователь вводит числа по одному, пока не введет слово "done". Для полученного списка
# чисел найдите среднее арифметическое. Для ввода используйте встроенную функцию input().
# numbers = []
# user_str = ''
# avg_arch = 0
# min_val = None
# max_val = None
# while user_str != 'done':
#     user_str = input('Введите число или для завершения - done:')
#     numbers.append(user_str)
# for val in numbers[:-1]:
#     avg_arch += int(val)
#     # 2. (1 балл)
#     # Напишите аналогичную программу, но для полученного списка найдите минимум и максимум.
#     if not min_val or int(val) <= min_val:
#         min_val=int(val)
#     elif not max_val or int(val) >= max_val:
#         max_val=int(val)
#     #
# avg_arch = avg_arch/len(numbers[:-1])
# print(avg_arch)
# print('max:%d , min:%d'%(max_val,min_val))
#

# 3. (2 балла, 1+1)
# На вход подается два словаря d1 и d2 с карточками продуктов (см. пример ниже). Необходимо объединить оба словаря в один
#  и удалить дубликаты значений (values в терминах метода dict()), если они есть, и вывести итоговый словарь.
# За объединение словаря 1 балл и еще 1 балл за корректное удаление дубликатов.
# При простом объединении словарей, если совпадают и ключи и значения, словарь сам убирает дубликаты.
#  В этом плане он похож на set(). Но наш случай не настолько тривиальный, у нас основные ключи разные, а значения,
#  то есть вложенные словари, могут быть одинаковыми. Вот как раз от одинаковых значений (вложенных словарей) надо избавиться.
#  Какой в итоге ему ключ будет присвоен из дубликатов - не имеет значения.
#
# d1 = {'Item1': {'Name': 'Cake', 'Price': 20},
#       'Item2': {'Name': 'Pie', 'Price': 10},
#       'Item3': {'Name': 'Chocobar', 'Price': 5}}
#
# d2={'Item4': {'Name': 'Brownie', 'Price': 15},
#     'Item5': {'Name': 'Cake', 'Price': 20}}
# union_dict = {}
# summ = 0
# union_keys = list(d1.keys()) + list(d2.keys())
# union_values = list(d1.values()) + list(d2.values())
# for key in union_keys:
#     for value in union_values:
#         if value not in union_dict.values():
#             union_dict[key]= value
# print(union_dict)

# 4. (1 балл)
# Для объединенного словаря из прошлого примера посчитайте итоговую сумму продуктов.
# for union_val in union_dict.values():
#     summ+=union_val['Price']
# print ('Sum of d products is:',summ)

# 5. (2 балла)
# Дан один словарь с запасами продуктов на складе. Дан второй словарь со стоимостью этих товаров. Создайте словарь с балансом этих продуктов.
d1={'Item1': 120, 'Item2': 100, 'Item3': 500}
d2={'Item1': 5, 'Item2': 12, 'Item3': 7}

balance = {}

for cost_key, cost_val in d1.items():
    for count_key, count_val in d2.items():
        if cost_key == count_key:
            balance[cost_key]=cost_val*count_val
print(balance)

