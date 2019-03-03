class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        max_to_here = 0
        max_so_far = 0

        for i in xrange(1, len(prices)):
            max_to_here = max(0, max_to_here + prices[i] - prices[i-1])
            max_so_far = max(max_so_far, max_to_here)

        return max_so_far


if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])