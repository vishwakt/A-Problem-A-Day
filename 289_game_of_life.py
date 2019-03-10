class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for i in range(0, rows):
            for j in range(0, cols):
                count = 0
                indices = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                for row, col in indices:
                    if 0 <= row < rows and 0<= col < cols:
                        if board[row][col] & 1:
                            count += 1

                    if board[i][j] == 1:
                        if count < 2 or count > 3:
                            continue
                        else:
                            board[i][j] |= 2
                    else:
                        if count == 3:
                            board[i][j] |= 2

        for i in range(0, rows):
            for j in range(0, cols):
                board[i][j] = board[i][j] >> 1


if __name__ == "__main__":
    s = Solution()
    print s.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])