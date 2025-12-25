import heapq
import networkx as nx
import matplotlib.pyplot as plt


def create_graph(graph_adj_list):
    result = {}

    for start_node, neighbors in graph_adj_list.items():
        if start_node not in result:
            result[start_node] = []

        for end_node, weight in neighbors.items():
            if end_node not in result:
                result[end_node] = []

            # Додаємо пряме ребро (якщо його ще немає)
            direct_edge = (end_node, weight)
            if direct_edge not in result[start_node]:
                result[start_node].append(direct_edge)

            # Додаємо зворотне ребро для неорієнтованого графа (якщо його ще немає)
            reverse_edge = (start_node, weight)
            if reverse_edge not in result[end_node]:
                result[end_node].append(reverse_edge)

    for node in result:
        result[node].sort()

    return result


def visualize_graph(graph_adj_list):
    graph = nx.Graph()
    graph.add_nodes_from(list(graph_adj_list))

    edges_with_weights = []
    for vertex, edges in graph_adj_list.items():
        for e, weight in edges.items():
            edges_with_weights.append((vertex, e, weight))
    graph.add_weighted_edges_from(edges_with_weights)

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def dijkstra(graph_adj_list, start):
    graph = create_graph(graph_adj_list)
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def main():
    graph_adj_list = {
        'A': {'B': 4, 'C': 2},
        'B': {'E': 3},
        'C': {'D': 2, 'F': 8},
        'D': {'E': 3, 'F': 1},
        'E': {'Z': 1},
        'F': {'Z': 3}
    }
    start_vertex = "A"
    distances = dijkstra(graph_adj_list, start_vertex)

    for vertex in distances:
        print(f"Відстань {start_vertex}-{vertex}: {distances[vertex]}")

    visualize_graph(graph_adj_list)


if __name__ == "__main__":
    main()
