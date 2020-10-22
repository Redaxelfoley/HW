# 1 задание

# Запрашиваем числа
try:
    first_num = int(input("Первое число: "))
    second_num = int(input("Второе число: "))
    result = first_num / second_num
    try:
        print("Частное {} и {} = {}".format(first_num, second_num, result))
    # Если пользователь пытается делить на ноль ему выдает ошибку.
    except ZeroDivisionError:
        print("Кажется вселенная начала процесс самоуничтожения... Не делите на ноль в следующий раз")
except ValueError:
    print("Ошибка ввода!")

# 2 задание


def usr_inf():
    city = input("Ваш город проживания: ")
    age = input("Ваш возраст: ")
    name = input("Ваше Ф.И.О: ")
    # Я думаю этого будет достаточно
    print("{} возрастом {} год(лет), проживает в городе {}".format(name, age, city))


usr_inf()
# 3 задание


def my_func(a, b, c):
    user_nums = [a, b, c]
    # Убираем самое маленькое число, и в итоге сумма двух больших чем оно чисел и является самой большой
    user_nums.remove(min(a, b, c))
    return sum(user_nums)


print(my_func(43,25,23))
# 4 задание


def exponentiation(d, z):
    return d ** z


print(exponentiation(45, -20))
# 5 задание


result = 0

while True:
    # Определяем переменные
    user_input = input("Введите числа через пробел или введите 'exit' для выхода из программы: ")
    # что бы из цикла выйти можно было
    if user_input == 'exit':
        break
    nums_arr = user_input.split()
    # Каждое число из новоиспеченного списка добовляем к результату
    for num in nums_arr:
        # Цикл for тут спасает, каждое число мы добавляем к результату, а если это и не число вовсе, выводим ошибку
        try:
            int_num = int(num)
            result += int_num
        except ValueError:
            print("Ошибка ввода!")
            print(result)
    print(result)
# 6 задание


def very_hard_func(text):
    # трудное задание требует трудных решений)
    print(text.title())


print(very_hard_func("it's really work lmao"))