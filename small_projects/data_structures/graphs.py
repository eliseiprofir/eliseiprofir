class DirectedGraph:
    def __init__(self) -> None:
        self.graph: dict = {}

    def add_edge(self, node_from: any, node_to: any) -> None:
        if node_from not in self.graph:
            self.graph[node_from]: list[any] = []
        if node_to not in self.graph:
            self.graph[node_from]: list[any] = []
        self.graph[node_from].append(node_to)


class WeightedDirectedGraph:
    def __init__(self) -> None:
        self.graph: dict = {}

    def add_edge(self, node_from: any, node_to: any, weight: int) -> None:
        if node_from not in self.graph:
            self.graph[node_from]: list[any] = []
        if node_to not in self.graph:
            self.graph[node_from]: list[any] = []
        self.graph[node_from].append((node_to, weight))


class UndirectedGraph:
    def __init__(self) -> None:
        self.graph: dict = {}

    def add_edge(self, node1: any, node2: any) -> None:
        if node1 not in self.graph:
            self.graph[node1]: list[any] = []
        if node2 not in self.graph:
            self.graph[node1]: list[any] = []
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)


class WeightedUndirectedGraph:
    def __init__(self) -> None:
        self.graph: dict = {}

    def add_edge(self, node1: any, node2: any, weight: int) -> None:
        if node1 not in self.graph:
            self.graph[node1]: list[any] = []
        if node2 not in self.graph:
            self.graph[node1]: list[any] = []
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))
