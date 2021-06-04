from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def DFS(i, graph, visited):
            if visited[i]:
                return
            else:
                visited[i] = 1
                for x in graph[i]:
                    DFS(x, graph, visited)

        visited = [0] * n
        graph = {x: [] for x in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        result = 0

        for i in range(n):
            if not visited[i]:
                DFS(i, graph, visited)
                result += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countComponents(n = 5, edges = [[0,1],[1,2],[3,4]]))