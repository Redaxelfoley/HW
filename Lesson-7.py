from abc import abstractmethod, ABC


# 1 Задание

class Matrix:

    def __init__(self, matrix: list):

        self.matrix_1 = matrix

    def __add__(self, other):

        result = [
            [
                self.matrix_1[row][idx] + other.matrix_1[row][idx]
                for idx in range(len(self.matrix_1))
            ]
            for row in range(len(self.matrix_1[0]))
        ]
        return Matrix(result)

    def __str__(self):

        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.matrix_1
        )


m1 = Matrix([
    [2, 44, 23],
    [1, 54, 98],
    [4, 87, 3]
])
m2 = Matrix([
    [1, 5, 65],
    [5, 4, 23],
    [13, 54, 26]
])

print(m1 + m2)
# 2 задание


class Cloth(ABC):

    def __init__(self, name: str):

        self.name = name

    @property
    @abstractmethod
    def calculate(self) -> float:

        pass


class Coat(Cloth, ABC):

    def __init__(self, name: str, size: float):

        super().__init__(name)
        self._size = size

    @property
    def calculate(self) -> float:
        return round(self._size / 6.5 + 0, 3)


class Suit(Cloth, ABC):

    def __init__(self, name: str, height: float):

        super().__init__(name)
        self._height = height

    @property
    def calculate(self) -> float:

        return round(2 * self._height + 0.3, 3)


ct = Coat("Пальто", 2)
print(ct.calculate)

st = Suit('Костюм', 0.8)
print(st.calculate)
# 3 задание


class Cell:
    __count: int

    def __init__(self, count: int):
        assert count > 0, "Количество ячеек должно быть больше 0"
        self.__count = count

    def __add__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count + other.count
        return Cell(value)

    def __sub__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count - other.count
        assert value > 0, "Разность ячеек меньше 0"
        return Cell(value)

    def __mul__(self, other: 'Cell'):
        self.validate_item(other)
        value = self.count * other.count
        return Cell(value)

    def __truediv__(self, other: 'Cell'):
        self.validate_item(other)
        value = round(self.count / self.count)
        return Cell(value)

    def __str__(self):
        return str(self.__count)

    def validate_item(self, other):
        assert isinstance(other, self.__class__), "Операции допустимы только между клетками"

    @property
    def count(self) -> int:
        return self.__count

    @staticmethod
    def make_order(cell_object: 'Cell', count_per_row: int) -> str:
        items = '*' * cell_object.count
        chunks = [
            items[idx:idx + count_per_row]
            for idx in range(0, len(items), count_per_row)
        ]

        return '\n'.join(chunks)


first = Cell(3)
second = Cell(2)
huge = Cell(12)

print(first + second)  # 3 + 2 = 5
print(first - second)  # 3 - 2 = 1
print(first * second)  # 3 * 2 = 6
print(first / second)  # 3 / 2 = 1 (округление)

print(Cell.make_order(huge, 5))
