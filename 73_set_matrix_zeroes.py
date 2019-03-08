class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return None
        index_of_zeros = []
        for index, rows in enumerate(matrix):
            for col_index, col in enumerate(rows):
                if col is 0:
                    matrix[index] = [0] * len(rows)
                    index_of_zeros.append(col_index)

        for row in matrix:
            for i in index_of_zeros:
                row[i] = 0


if __name__ == "__main__":
    s = Solution()
    print s.setZeroes([
  [1,1,1],
  [1,0,0],
  [1,1,1]
])