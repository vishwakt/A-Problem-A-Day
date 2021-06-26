from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        curArrayIndex = None

        for i in range(len(matrix)):
            if target < matrix[i][0]:
                curArrayIndex = i - 1
                break

        print(curArrayIndex)
        if curArrayIndex is None:
            curArrayIndex = len(matrix)-1
        if curArrayIndex < 0:
            curArrayIndex = 0

        for j in range(len(matrix[curArrayIndex])):
            if matrix[curArrayIndex][j] == target:
                print(matrix[curArrayIndex][j])
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix(matrix = [[1],[3]], target = 1))