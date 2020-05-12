import collections


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rottenQueue = collections.deque([])
        freshCount = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    freshCount += 1
                if grid[i][j] == 2:
                    rottenQueue.append((i, j))

        time = 0

        while rottenQueue:
            for _ in range(len(rottenQueue)):
                i, j = rottenQueue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        freshCount -= 1
                        rottenQueue.append((x, y))

            time += 1

        if freshCount == 0:
            return max(0, time-1)
        else:
            return -1


if __name__ == "__main__":
    s = Solution()
    print s.orangesRotting(grid=[[2,1,1],[1,1,0],[0,1,1]])