class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            # print zip([0] + row, row + [0])
            row = [x + y for x, y in zip([0] + row, row + [0])]
            # print row
        return row


if __name__ == "__main__":
    s = Solution()
    print s.getRow(7)