# Time complexity: O(V+E)
from queue import Queue


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

            if not current.destination in self.dict[current.source]:
                self.dict[current.source].append(current.destination)

            if not current.destination in self.dict:
                self.dict[current.destination] = []

            if not current.source in self.dict[current.destination]:
                self.dict[current.destination].append(current.source)

    def print(self):
        for src in self.dict:
            for dest in self.dict[src]:
                print(f"({src} -> {dest}) ", end="")
            print()

    def nodes_length(self):
        return len(self.dict.keys())

    def get(self):
        return self.dict


def bfs(graph, start):
    if not start in graph.keys():
        return

    q = Queue()
    q.put(start)
    visited = {}
    visited[start] = True

    while not q.empty():
        current = q.get()
        print(f'visiting {current}')

        for neighbour in graph[current]:
            if not neighbour in visited:
                visited[neighbour] = True
                q.put(neighbour)


if __name__ == "__main__":
    edges = [Edge(0, 9), Edge(0, 7), Edge(0, 11), Edge(9, 10), Edge(9, 8), Edge(7, 3), Edge(7, 6),
             Edge(11, 7), Edge(10, 1), Edge(8, 1), Edge(8, 12), Edge(12, 2), Edge(3, 2), Edge(3, 4), Edge(6, 5)]

    graph = Graph(edges)
    bfs(graph.get(), 0)
