class Node:
    def __init__(self, value: any) -> None:
        self.value: any = value
        self.right: Node | None = None
        self.left: Node | None = None


class BinaryTree:
    def __init__(self, root_value: any) -> None:
        self.root: Node = Node(root_value)

    def append_right(self, value: any) -> None:
        self.root.right = Node(value)

    def append_left(self, value: any) -> None:
        self.root.left = Node(value)

    def insert(self, value: any) -> None:
        if not self.root:
            self.root: Node = Node(value)
            return

        current: Node = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    break
                current = current.left

            if value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    break
                current = current.right

            else:
                break

    def delete(self, value):
        parent: Node | None = None
        current: Node = self.root

        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if current is None:
            return

        if current.left is None or current.right is None:
            new_current = None
            if current.left is not None:
                new_current = current.left
            if current.right is not None:
                new_current = current.right

            if parent is None:
                self.root = new_current

            if current == parent.left:
                parent.left = new_current
            if current == parent.right:
                parent.right = new_current

        else:
            p: Node | None = None

            temp: Node = current.right
            while temp.left is not None:
                p = temp
                temp = temp.left

            if p is not None:
                p.left = temp.right
            else:
                current.right = temp.right

            current.value = temp.value
