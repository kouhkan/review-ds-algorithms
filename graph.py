from collections import deque


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)

    def dfs(self, start):
        visited = set()

        def dfs_util(node):
            visited.add(node)
            print(node)

            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs_util(neighbor)

        dfs_util(start)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node)
                visited.add(node)
                for neighbor in self.adj_list.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)

print("DFS Traversal:")
graph.dfs(1)


print("BFS Traversal:")
graph.bfs(1)