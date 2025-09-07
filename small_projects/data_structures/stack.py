class Stack:
    def __init__(self) -> None:
        self.__items: list[any] = []

    def push(self, item: any) -> None:
        self.__items.append(item)

    def pop(self) -> any:
        if not self.is_empty():
            return self.__items.pop()

    def peek(self) -> any:
        if not self.is_empty():
            return self.__items[-1]

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        return len(self.__items)

    def clear(self) -> None:
        self.__items = []

    def to_list(self) -> list[any]:
        return self.__items

    def min(self) -> any:
        if not self.is_empty():
            return min(self.__items)

    def max(self) -> any:
        if not self.is_empty():
            return max(self.__items)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    print(stack.to_list())

    stack.push(2)
    print(stack.to_list())

    stack.push(3)
    print(stack.to_list())

    stack.push(4)
    print(stack.to_list())

    stack.pop()
    print(stack.to_list())

    print(f"Peek - {stack.peek()}")
    print(f"Empty? - {stack.is_empty()}")
    print(f"Size - {stack.size()}")
    print(f"Min - {stack.min()}")
    print(f"Max - {stack.max()}")
    print(f"To list - {stack.to_list()}")
