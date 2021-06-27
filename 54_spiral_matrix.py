from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        if len(matrix) == 0:
            return result

        rowBegin = 0
        colBegin = 0
        rowEnd = len(matrix) - 1
        colEnd = len(matrix[0]) - 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                result.append(matrix[rowBegin][i])
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):
                result.append(matrix[i][colEnd])
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    result.append(matrix[rowEnd][i])
                rowEnd -= 1
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    result.append(matrix[i][colBegin])
                colBegin += 1

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder( matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))