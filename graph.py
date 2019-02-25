from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print s

            for i in self.graph[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):
        visited[v] = True
        print v
        for i in self.graph[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * len(self.graph)

        self.DFSUtil(v, visited)


if __name__ == "__main__":
    g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)

    # g.BFS(3)

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)