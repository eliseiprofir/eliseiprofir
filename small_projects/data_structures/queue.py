from collections import deque


class Queue:
    def __init__(self, items=None) -> None:
        if items is None:
            items = []
        self.__items: deque[any] = deque(items)

    def enqueue(self, item: any) -> None:
        self.__items.append(item)

    def dequeue(self) -> any:
        if not self.is_empty():
            return self.__items.popleft()

    def peek(self) -> any:
        if not self.is_empty():
            return self.__items[0]

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def size(self) -> int:
        return len(self.__items)

    def clear(self) -> None:
        self.__items = []

    def contains(self, item: any) -> bool:
        return self.__items.count(item) > 0

    def reverse(self) -> None:
        self.__items.reverse()

    def show(self) -> deque[any]:
        return self.__items

    def to_list(self) -> list[any]:
        temp_queue = Queue(self.__items)
        lst = []
        while not temp_queue.is_empty():
            lst.append(temp_queue.dequeue())
        return lst


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    print(queue.show())

    queue.enqueue(2)
    print(queue.show())

    queue.enqueue(3)
    print(queue.show())

    queue.enqueue(4)
    print(queue.show())

    queue.dequeue()
    print(queue.show())

    queue.reverse()
    print(queue.show())

    print(queue.is_empty())

    print(f"Peek - {queue.peek()}")
    print(f"Empty? - {queue.is_empty()}")
    print(f"Size - {queue.size()}")
    print(f"Contains 1 - {queue.contains(1)}")
    print(f"Contains 2 - {queue.contains(2)}")
    print(f"To list - {queue.to_list()}")
