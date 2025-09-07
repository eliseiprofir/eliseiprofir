my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def shortest_path(graph, start, target = ''):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths

shortest_path(my_graph, 'A', 'F')

# import networkx as nx
# import matplotlib.pyplot as plt

# my_graph = {
#     'A': [('B', 5), ('C', 3), ('E', 11)],
#     'B': [('A', 5), ('C', 1), ('F', 2)],
#     'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
#     'D': [('C', 1), ('E', 9), ('F', 3)],
#     'E': [('A', 11), ('C', 5), ('D', 9)],
#     'F': [('B', 2), ('D', 3)]
# }

# def draw_graph(graph):
#     G = nx.Graph()
#     for node, edges in graph.items():
#         for edge, weight in edges:
#             G.add_edge(node, edge, weight=weight)

#     pos = nx.spring_layout(G)  # Layout-ul grafului

#     nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')  # Desenarea grafului
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # Afișarea ponderilor muchiilor
#     plt.show()

# draw_graph(my_graph)
