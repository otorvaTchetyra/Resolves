# Задача 1 (просто) "Арифметика"
# 1st program
result1 = 9 ** 0.5 * 5
print(result1)  # Ожидаемый результат: 15.0

# Задача 2 (просто) "Логика"
# 2nd program
result2 = 9.99 > 9.98 and 1000 != 1000.1
print(result2)  # Ожидаемый результат: True

# Задача 3 (средне) "Школьная загадка"
# 3rd program
result3_1 = 2 * 2 + 2  # Без приоритета
result3_2 = 2 * (2 + 2)  # С приоритетом
print(result3_1)  # Выводим первое выражение
print(result3_2)  # Выводим второе выражение
result3_comparison = result3_1 == result3_2
print(result3_comparison)  # Ожидаемый результат: False

# Задача 4 (сложно) "Первый после точки"
# 4th program
number_str = '123.456'
number_float = float(number_str)  # Преобразуем строку в дробное число
shifted_number = number_float * 10  # Умножаем на 10
integer_part = int(shifted_number)  # Берем целую часть
first_digit_after_decimal = integer_part % 10  # Находим первую цифру после запятой
print(first_digit_after_decimal)  # Ожидаемый результат: 4
