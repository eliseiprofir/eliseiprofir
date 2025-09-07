class Node:
    def __init__(self, value: any) -> None:
        self.value: any = value
        self.next: Node | None = None

    def __str__(self) -> str:
        after = self.next.value if self.next else None
        return f"{self.value}(->{after})"

    def __repr__(self) -> str:
        after = self.next.value if self.next else None
        return f"value={self.value} - next={after}"


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None

    def append(self, value: any) -> None:
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node: Node | None = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, index: int, value: any) -> None:
        if not index:
            print("The given previous node must be in the LinkedList.")
            return
        current_node: Node | None = self.head
        count: int = 0
        while index != count + 1:
            current_node = current_node.next
            count += 1
        new_node: Node = Node(value)
        new_node.next = current_node.next
        current_node.next = new_node

    def find(self, value: int) -> str:
        current_node: Node | None = self.head
        if current_node and current_node.value == value:
            return f"'{current_node.value}' found at index 0."

        index: int = 0
        while current_node and current_node.value != value:
            current_node = current_node.next
            index += 1

        if current_node is None:
            return "Not found."
        return f"'{current_node.value}' found at index {index}."

    def get(self, index: int) -> any:
        if index < 0:
            return None

        count: int = 0
        current_node: Node = self.head
        while current_node:
            if count == index:
                return current_node.value
            current_node = current_node.next
            count += 1

        return None

    def delete(self, value: int) -> None:
        current_node: Node | None = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        prev_node: Node | None = None
        while current_node and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def __str__(self) -> str:
        current_node: Node | None = self.head
        formatted: str = ""
        while current_node is not None:
            formatted += f"{str(current_node.value)}, "
            current_node = current_node.next
        formatted = formatted[:-2]
        return f"[{formatted}]"

    def __repr__(self) -> str:
        current_node: Node | None = self.head
        formatted: str = ""
        while current_node is not None:
            formatted += f"{str(current_node)}, "
            current_node = current_node.next
        formatted = formatted[:-2]
        return f"[{formatted}]"


if __name__ == "__main__":
    lst = LinkedList()
    print("Inserting...")
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    print(lst)
    print(lst.__repr__())
    print()

    print("Deleting 3...")
    lst.delete(3)
    print(lst)
    print(lst.__repr__())
    print()

    print("Getting, finding...")
    print(lst.get(0))
    print(lst.find(1))
    print()

    print("Inserting 3 at index 2")
    lst.insert(2, 3)
    print(lst)
    print(lst.__repr__())
    print()

    print("Inserting 3 at index 1")
    lst.insert(1, 3)
    print(lst)
    print(lst.__repr__())
