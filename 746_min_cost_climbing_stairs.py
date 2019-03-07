class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        num_of_stairs = len(cost)
        if num_of_stairs is 0:
            return 0
        elif num_of_stairs is 1:
            return cost[0]
        elif num_of_stairs is 2:
            return min(cost[0], cost[1])
        else:
            for i in range(2, num_of_stairs):
                cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])


if __name__ == "__main__":
    s = Solution()
    print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])