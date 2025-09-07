class MinHeap:
    def __init__(self, items: list[any]) -> None:
        if items:
            self.heap: list[any] = items
        else:
            self.heap: list[any] = []

    def push(self, value: any) -> None:
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index: int) -> None:
        parent: int = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def pop(self) -> any:
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        root: any = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self._bubble_down(0)
        return root

    def _bubble_down(self, index: int) -> None:
        min: int = index
        left: int = self._left_child(min)
        right: int = self._right_child(min)

        if left < len(self.heap) and self.heap[left] < self.heap[min]:
            min = left
        if right < len(self.heap) and self.heap[right] < self.heap[min]:
            min = right

        if min != index:
            self.heap[index], self.heap[min] = self.heap[min], self.heap[index]
            self._bubble_down(min)

    def peek(self) -> any:
        return self.heap[0] if self.heap else None

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2
