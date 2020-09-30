# Time complexity: O(V+E)
class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


class Graph:
    def __init__(self, edges):
        self.dict = {}

        for current in edges:
            if not current.source in self.dict:
                self.dict[current.source] = []

            self.dict[current.source].append(current.destination)

    def print(self):
        for src in self.dict:
            for dest in self.dict[src]:
                print(f"({src} -> {dest}) ", end="")
            print()

    def nodes_length(self):
        return len(self.dict.keys())

    def get(self):
        return self.dict


def dfs(graph, at):
    if visited[at]:
        return

    visited[at] = True
    print(f'visiting {at}')

    if not at in graph.keys():
        return

    neighbours = graph[at]
    for next in neighbours:
        dfs(graph, next)


if __name__ == "__main__":
    edges = [Edge(0, 9), Edge(9, 8), Edge(8, 1), Edge(1, 0), Edge(8, 7), Edge(7, 10), Edge(
        10, 11), Edge(11, 7), Edge(7, 3), Edge(3, 2), Edge(3, 4), Edge(3, 5), Edge(5, 6), Edge(6, 7)]

    graph = Graph(edges)
    graph.print()

    visited = [False] * 12
    dfs(graph.get(), 0)
