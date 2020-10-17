# Практическую работу выполнил Косолапов Кирилл
# Первое задание

# Обьявляем список с различнысм типами данных
test_arr = ['str', 1, 5000, '50', b'bytes', [], (), {}]

# Создаем проверку типа каждого обьекта находящегося в списке
for obj in test_arr:
    print(type(obj))

# Второе задание


# Введеные пользователем значения, будут добавлены в список
user_values = input("Введите значения для вашего списка через запятые: ")

# Делим ввод пользователя на элементы нового списка через запятую
user_arr = user_values.split(',')

"""
Пытался я сделать через while но он никак не хочет работать.
value = 0
n = 0

while n > len(user_arr):
    if len(user_arr) % 10 != 0:
        if n == len(user_arr):
            break
    user_arr[value], user_arr[value + 1] = user_arr[value + 1], user_arr[value]
    value += 2
    n += 1

print(user_arr)
"""
num = 0

# Перебираем все элементы списка попутно меняя их местами

for i in range(int(len(user_arr) / 2)):
    user_arr[num], user_arr[num + 1] = user_arr[num + 1], user_arr[num]
    num += 2

print(user_arr)

# Третье задание

months = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}
user_month = int(input("Введите цифру вашего месяца, учтите что она должна быть целым числом от 1 до 12: "))
print(months[user_month])

# Другой способ, как по мне куда более компактный
if user_month == 1 or user_month == 2 or user_month == 12:
    print('Зима')
elif 3 <= user_month <= 5:
    print('Весна')
elif 6 <= user_month <= 8:
    print('Лето')
elif 9 <= user_month <= 11:
    print('Осень')

# Четвертое задание

user_words = input("Введите ваши слова через пробел: ")

# Снова использую читерный сплит что бы разделить слова на обьекты для словаря
words_arr = user_words.split(' ')

# А теперь просто вывожу их, и используя срез не допускаю слов длиннее 10 символов
for word in words_arr:
    print(word[:10])

# Пятое задание

natural_list = [7, 5, 3, 3, 2]

user_num = int(input("Введите натуральное число: "))

if user_num > max(natural_list):
    natural_list.insert(0, user_num)
elif user_num < min(natural_list):
    natural_list.append(user_num)
else:
    for i in natural_list:
        if i == user_num:
            indx = natural_list.index(user_num)
            natural_list.insert(indx, user_num)
            break

print(natural_list)

# Не совсем понял как сделать так что бы даже не существующее в списке число заняло правильное место в рейтинге
# Например [5,5,4,2,2,1] как сюда влепить 3? что бы она стояла между 4 и 2

# Шестое задание

while True:
    name = input("Название товара: ")
    cost = input("Цена товара: ")
    quantity = input("Кол-во товара на складе: ")
    form = input("Кол-во чего? шт. например: ")

    product = {
        'название': name,
        'цена': cost,
        'количество': quantity,
        'ед': form
    }
    print(product.items())

    quit = input("Если хотите выйти напишите 'quit': ")

    if quit == 'quit':
        break
    else:
        print(product.items())
        continue
# Надеюсь справился, спасибо за Практическое задание! До встречи на 3 уроке!
