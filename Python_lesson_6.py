# Урок 6. ТИПИЗАЦИЯ ДАННЫХ

# one1 = '123'  # Перевод строки  в число
# two = int(one1)
# print(type(two))
#
# op = 12  # Перевод числа в строку
# joi = str(op)
# print(type(joi))
#
# epr = '354'  # Перевод строки к числу с плавающей точкой
# pip = float(epr)
# print(type(pip))
#
# Неправильный код
# first = "5"
# second = 7
# third = first + second
# print(third)  # В данном примере код выдаст ошибку, т.к нужно строку примести к функции int(first)
#
# Прильный код
# first = "5"
# second = 7
# third = int(first) + second
# print(third)  # Правильный код, т.к мы строку first привели к числу с помощбю функции int()
#
# number1 = 2.0001
# number2 = 5
# number3 = number1 / number2
# print(number3)  # результат с дробными числами может быть не совсем точными
#
# round - ЭТО ФУНКЦИЯ ДЛЯ ОКРУГЛЕНИЯ РЕЗУЛЬТАТА
# number1 = 2.0001
# number2 = 0.1
# number3 = number1 + number2
# print(round(number3, 4))  # первый параметр округляемое значение, второе сколько знаков после запятой должно быть
#
#  ПРЕОБРАЗОВАНИЕ ЧИСЕЛ В СТРОКИ
# one = 5
# print(str(one))  # преобразовали переменную из числа в строку
#
# yesterday = '50'
# today = '150'
# more = int(today) - int(yesterday)
# print(more)
#
#  РАБОТА С ДРРОБНЫМИ ВЫРАЖЕНИЯМИ
# method_1 = "55.12"
# method_2 = "78.69"
# method_3 = method_1 + method_2
# print(method_3)  # в данном коде происходит конкагстинация строк при помощи оператора +
# # Поэтому нужно привести строки к дробным числам
# point_1 = '55.12'
# point_2 = '78.69'
# point_3 = float(point_1) + float(point_2)
# print(point_3)
