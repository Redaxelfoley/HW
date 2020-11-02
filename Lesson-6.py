from time import sleep


# 1 задание


class TrafficLight:
    __lights = ['Красный', 'Жёлтый', 'Зелёный']

    def run_work(self):
        i = 0
        while i != 3:
            print(TrafficLight.__lights[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


t = TrafficLight()
t.run_work()


# 2 задание


class Road:

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self.weight = 25
        self._height = height

    def mass_calc(self):
        print(self._length * self._width * 25 * self._height)


r = Road(50, 20, 2)
r.mass_calc()


# 3 задание


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.surname = surname
        self.name = name
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


p = Position('Dungeon', 'Master', 'WebDesigner', '1000', '1043')
print(p.get_full_name(), p.get_total_income())


# 4 задание


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nYour speed is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())


# 5 задание
# Не понял смысл делать 3 дочерних класса, если при вызове функции можно указать чем будет отрисованно
# маркером, карандашем или же ручкой
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


s = Stationary('карандашем')
print(s.draw())
s = Stationary('маркером')
print(s.draw())
s = Stationary('ручкой')
print(s.draw())
# Возможно я выполнил задание не правильно, но я так вижу правильный вариант исполнения этого задания
