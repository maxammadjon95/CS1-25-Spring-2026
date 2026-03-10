from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, c: str):
        self.color = c

    def get_color(self) -> str:
        return self.color

    @abstractmethod
    def get_area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, c: str, side: float):
        super().__init__(c)
        self.side = side

    def get_area(self) -> float:
        return self.side * self.side


if __name__ == "__main__":
    color = "red"
    side = 5.0

    square = Square(color, side)

    print(square.get_color(), square.get_area())