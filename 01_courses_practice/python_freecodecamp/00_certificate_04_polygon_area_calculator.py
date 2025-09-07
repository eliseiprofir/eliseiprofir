class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> int:
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture: str = ""
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape: 'Rectangle') -> int:
        return (self.width // shape.width) * (self.height // shape.height)

    def set_height(self, height: int) -> None:
        self.height: int = height

    def set_width(self, width: int) -> None:
        self.width: int = width

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.side: int = side
        super().__init__(side, side)

    def set_side(self, side: int) -> None:
        self.side: int = side
        self.width: int = side
        self.height: int = side

    def set_height(self, height: int) -> None:
        self.set_side(height)

    def set_width(self, width: int) -> None:
        self.set_side(width)

    def __str__(self) -> str:
        return f"Square(side={self.side})"


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
