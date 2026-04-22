# GRAPH IMPLEMENTATIONS
from collections import deque
import heapq


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # BFS
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))

    # DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Cycle Detection (Directed)
    def has_cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False

    # Topological Sort
    def topological_sort(self):
        visited = set()
        stack = []

        def dfs(node):
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)

        for node in self.graph:
            if node not in visited:
                dfs(node)

        return stack[::-1]

    # Dijkstra
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        pq = [(0, start)]

        while pq:
            dist, node = heapq.heappop(pq)

            for neighbor, weight in self.graph.get(node, []):
                new_dist = dist + weight
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        return distances


# MAIN
if __name__ == "__main__":
    g = Graph()

    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    print("BFS:")
    g.bfs(1)

    print("\nDFS:")
    g.dfs(1)

    print("\nCycle:", g.has_cycle())

    print("Topological Sort:", g.topological_sort())

    g2 = Graph()
    g2.graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }

    print("Dijkstra from A:", g2.dijkstra('A'))