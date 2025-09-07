class MaxHeap:
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
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index: int = parent
            parent = self._parent(index)

    def pop(self) -> any:
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()

        max: any = self.heap[0]
        self.heap[0] = self.heap.pop(-1)
        self._bubble_down(0)
        return max

    def _bubble_down(self, index: int) -> None:
        max: int = index
        left: int = self._left_child(max)
        right: int = self._right_child(max)

        if left < len(self.heap) and self.heap[left] > self.heap[max]:
            max = left
        if right < len(self.heap) and self.heap[right] > self.heap[max]:
            max = right

        if max != index:
            self.heap[index], self.heap[max] = self.heap[max], self.heap[index]
            self._bubble_down(max)

    def peek(self) -> any:
        return self.heap[0] if self.heap else None

    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2
