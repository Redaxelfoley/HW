# 1-ое задание

example_var_1 = 1
example_var_2 = 242

print(example_var_1 + example_var_2)
print(example_var_2)

user_var_int = int(input("Ваше число: "))
user_var_str = input("Ваша строка: ")

print("Ваше число: {}, Ваша строка: {}".format(user_var_int, user_var_str))

# 2-ое задание

user_sec = int(input("Введите время в секундах: "))

hour = user_sec // 60
min = user_sec // 60 // 60
sec = user_sec % 60

if len(str(hour)) < 2:
    hour = '0' + str(hour)
if len(str(min)) < 2:
    min = '0' + str(min)
if len(str(sec)) < 2:
    sec = '0' + str(sec)

print("{}:{}:{}".format(hour, min, sec))

# 3-е задание

n = int(input('Введите число: '))

print(n + n * 11 + n * 111)

# 4-ое задание

user_num = int(input("Введите целое положительное число: "))
mx = 0

while user_num > 0:
    n = user_num % 10
    if n > mx:
        mx = n
    user_num //= 10
print(mx)

# 5-ое задание

revenue = int(input("Выручка вашей компании: "))
cost = int(input("Издержки вашей компании: "))
profit = revenue - cost

try:
    part = revenue / profit
except:
    print("Вы ушли в ноль!")

if profit > 0:
    print("Ваша компания имеет прибыль\n она составила {}руб.".format(profit))
    print("Это {} часть от выручки".format(round(part, 2)))
    staff = int(input("Кол-во сотрудников вашей компании: "))
    print(profit // staff, 'руб каждому сотруднику')
elif profit < 0:
    print("Ваша компания в убытке!")

# 6-ое задание

result = int(input("Результат спортсмена в первый день: "))
x_day = int(input("Результат спортсмена в итоге: "))
day = 1

if result > x_day:
    print("Что-то ваш спортсмен слабак")

while result <= x_day:
    print('{}-ый день: {}км'.format(day, round(result, 2)))
    day += 1
    result *= 1.10
print("На {} день спортсмен пробежал {}км".format(day, x_day))

# Спасибо за обучение!
