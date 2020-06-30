"""
        6          5
    A ------- B ------- C
    |        /|        /
  1 |   2  /  | 2    /  5
    |    /    |    /
    |  /      |  /
    |/        |/
    D ------- E
        1

Dijkstra解决有向/无向图最短路径问题(无法在负权值上运行, 但Bellman-Ford算法能), 计算所有节点到A的最短路径, 时间复杂度为O(n^2)
"""


def dijkstra(graph, node, connected):
    items = list(connected.keys())
    shortest_distance = {}
    previous_vertex = {}
    for k in items:
        shortest_distance[k] = float('inf')

    visited = [node]
    shortest_distance[node] = 0
    previous_vertex[node] = node
    stack = [node]
    unvisited = items

    while len(unvisited) > 0:
        cur = stack.pop()
        for k in connected[cur]:
            if k not in visited:
                stack.append(k)

                d = graph[(cur, k)] + shortest_distance[cur]
                if d < shortest_distance[k]:
                    shortest_distance[k] = d
                    previous_vertex[k] = cur
        visited.append(cur)
        unvisited.remove(cur)
    return shortest_distance, previous_vertex


def show_path(previous_vertex, node):
    for key, _ in previous_vertex.items():
        while key != node:
            print(key + " -> ", end="")
            key = previous_vertex[key]
        print(node)


if __name__ == "__main__":
    graph_ = {}
    graph_[("A", "D")] = 1
    graph_[("A", "B")] = 6
    graph_[("B", "C")] = 5
    graph_[("B", "D")] = 2
    graph_[("B", "E")] = 2
    graph_[("C", "E")] = 5
    graph_[("D", "E")] = 1

    graph = {}
    for key, val in graph_.items():
        graph[key] = val
        graph[(key[1], key[0])] = val

    connected = {}
    connected["A"] = ["B", "D"]
    connected["B"] = ["A", "C", "D", "E"]
    connected["C"] = ["B", "E"]
    connected["D"] = ["A", "B", "E"]
    connected["E"] = ["B", "C", "D"]

    node = "A"
    shortest_distance, previous_vertex = dijkstra(graph, node, connected)
    print(shortest_distance)
    # print(previous_vertex)
    show_path(previous_vertex, node)