import json as j
# 1 задание

with open('first', 'w') as f:
    while True:
        inp = input(": ")
        f.write(f"{inp} ")
        if inp == "":
            break
# 2 задание
with open('second', 'r') as s:
    c_lines = 0
    c_letters = 0
    for line in s:
        c_lines += 1
        c_letters = len(line)
        print(f"Кол-во символов в {c_lines} строке : ", c_letters)
    print("Строки: ", c_lines)
# 3 задание

with open('third', 'r') as t:
    sr_ar = []
    for line in t:
        r = line.split()
        name = r[0]
        surname = r[1]
        pay = int(r[2])
        if pay < 20000:
            print(f"Сотрудник {name} {surname} имеет зарплату ниже 20тыс.")
        sr_ar.append(pay)
    print(f"Средняя зарплата сотрудников составляет: {sum(sr_ar) // len(sr_ar)}руб.")
# 4 задание

nums = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Ten': 'Десять'
}
with open('four', 'r') as four:
    with open('four_2', 'w') as f2:
        for line in four:
            f_r = line.split()
            if f_r[0] in nums:
                f_r[0] = nums[f_r[0]]
                f2.writelines(f"{f_r}\n")
            else:
                print('Произошла ошибка!')
# 5 задание

with open('five', 'w') as fiv:
    f_nums = [1, 54, 23, 20, 11]
    fiv.writelines(str(f_nums))
    print(f'Сумма всех чисел в файле: {sum(f_nums)}')
# 6 задание

"""
К сожалению не понял как решить это задание, буду рад если вы подскажете!
"""
# 7 задание

with open('seven', 'r') as svn:
    final = [[]]
    prof_f = {}
    costs = []
    sr_ar2_1 = []
    sr_ar2_2 = {}
    for line in svn:
        r = line.split()
        name = r[0]
        form = r[1]
        revenue = int(r[2])
        cost = int(r[3])
        profit = revenue - cost
        sr_ar2_1.append(profit)
        if profit < 0:
            final[0].append(name)
        else:
            prof_f[name] = profit
    true_average = sum(sr_ar2_1) // len(sr_ar2_1)
    sr_ar2_2['average_profit'] = true_average
    final.append(sr_ar2_2)
    final.append(prof_f)


with open('seven_2', 'w') as svn_2:
    j.dump(final, svn_2)
