class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for _ in range(0, n+1)]
        result[0], result[1] = 1, 1
        for x in range(2, n+1):
            y = 1
            while y<=2:
                result[x] = result[x] + result[x-y]
                y=y+1
        return result[n]


stairs = Solution()
print(stairs.climbStairs(5))