class Node:
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self.type: str = type  # 'file' or 'folder'
        self.children: list[any] = []  # List of Node objects

    def is_folder(self) -> bool:
        return self.type == 'folder'

    def is_file(self) -> bool:
        return self.type == 'file'


class FileSystem:
    def __init__(self) -> None:
        self.root: Node = Node("root", "folder")

    def _find_path(self, path: str) -> Node | None:
        paths: list[str] = path.strip("/").split("/")
        current: Node = self.root

        if len(paths) == 1 and paths[0] == "":
            return self.root

        for path in paths:
            found: bool = False
            for child in current.children:
                if child.name == path:
                    current = child
                    found = True
            if not found:
                return None
        return current

    def create(self, path: str, name: str, type: str) -> None:
        location: Node | None = self._find_path(path)
        if location is None or location.is_file():
            print(f"Error: Path '{path}' not found or is not a directory.")
            return

        for child in location.children:
            if child.name == name:
                print(f"Error: '{name}' already exists in '{location}'.")
                return

        new_node: Node = Node(name, type)
        location.children.append(new_node)
        print(f"'{name}' created successfully at '{location}'.")

    def read(self, path: str) -> None:
        location: Node | None = self._find_path(path)
        if location is None:
            print(f"Error: Path '{path}' not found.")
            return
        print(f"Showing content from the folder '{location.name}'")
        for child in location.children:
            print(f"- {str(child.type).capitalize()} '{child.name}'.")

    def update(self, path: str, new_name: str) -> None:
        node: Node = self._find_path(path)
        if node is None:
            print(f"Error: Path '{path}' not found.")
            return

        node.name = new_name
        print(f"'{path}' renamed successfully to '{new_name}'.")

    def delete(self, path: str) -> None:
        paths: list[str] = path.strip("/").split("/")
        if len(paths) == 0:
            print("Error: Invalid path.")
            return

        parent_path: str = "/".join(paths[:-1])
        node_name: str = paths[-1]

        parent: Node | None = self._find_path(parent_path)
        if parent is None or not parent.is_folder():
            print(f"Error: Path '{parent_path} not found or is not a directory.")
            return

        node_to_delete: Node | None = None
        for child in parent.children:
            if child.name == node_name:
                node_to_delete = child
                break

        if node_to_delete is None:
            print(f"Error: '{node_name} not found in '{parent_path}.")
            return

        parent.children.remove(node_to_delete)
        print(f"'{node_name}' deleted successfully from '{parent_path}'.")

    def print_file_system(self, node: Node | None = None, indent: str = ""):
        """Print the file system structure starting from a given node."""
        if node is None:
            node = self.root

        # Print the current node's name
        print(indent + node.name + " (" + node.type + ")")

        # If it's a folder, recursively print its children with indentation
        if node.is_folder():
            for child in node.children:
                self.print_file_system(child, indent + "    ")


if __name__ == "__main__":
    fs = FileSystem()

    # Create directories and files
    fs.create("/", "folder1", "folder")
    fs.create("/folder1", "file1.txt", "file")
    fs.create("/folder1", "folder2", "folder")

    # Read directory contents
    fs.read("/")  # Should list folder1
    fs.read("/folder1")  # Should list file1.txt and folder2

    # Update file/folder name
    fs.update("/folder1/file1.txt", "new_file1.txt")

    # Read after update
    fs.read("/folder1")  # Should list new_file1.txt and folder2

    # Delete a file
    fs.delete("/folder1/new_file1.txt")
    fs.read("/folder1")  # Should list only folder2

    # Delete a folder
    fs.delete("/folder1/folder2")
    fs.read("/folder1")  # Should be empty now

    # Printing files and folders
    fs.print_file_system()
