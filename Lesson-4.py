from functools import reduce
from math import factorial
# 1 задание


def pay_calc(hrs, cst, prm):
    # Узнаем зарплату путем вычислений и прибавляем премию.
    pay = hrs * cst
    return pay + prm


print(pay_calc(5, 500, 1000))
# 2 задание


# Создаем словарики
arr = [123, 22, 10, 2, 2, 3, 10, 1, 555, 228]
result_arr = []
for i in range(1, len(arr)):
    # Смотрим больше ли число чем прошлое и добавлять ли его в словарь
    if arr[i] > arr[i - 1]:
        result_arr.append(arr[i])
print(result_arr)

# 3 задание


new_arr = [el for el in range(20, 241) if (el % 20) == 0 or (el % 21) == 0]
print(new_arr)
# 4 задание


hw_arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
four_arr =  [z for z in hw_arr if hw_arr.count(z) < 2]

print(four_arr)
# 5 задание


five_arr = [c for c in range(100, 1001) if (c % 2) == 0]
# Умножаем все
sum_all = reduce(lambda x, y: x + y, five_arr)
print(sum_all)
# 6 задание

# 1
f_num = int(input("Введите начальное число: "))
# Генерируем словарь
a = [i for i in range(f_num, 10)]
iterator = iter(a)
while True:
    try:
        # Итерируем числа
        out = next(iterator)
        print(out)
    except StopIteration:
        # После достижения 10 итерация заканчивается
        print("Конец итерации!")
        break
# 2


emp_arr = [92, 1, 40, 2, 5]
iterator_2 = iter(emp_arr)
while True:
    try:
        # Итерируем числа
        v = next(iterator_2)
        # Так можно?)
        print(v, v)
    except StopIteration:
        # После достижения 10 итерация заканчивается
        print("Конец итерации!")
        break
# 7 Задание


def gen(h):
    n = factorial(h)
    yield n
# А теперь тестируем нашу функцию


ready_test_arr = [d for d in gen(int(input("Факториал числа: ")))]
print(ready_test_arr)
