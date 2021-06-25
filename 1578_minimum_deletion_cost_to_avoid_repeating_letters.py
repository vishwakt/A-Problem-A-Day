from typing import List

'''
Intuition
For a group of continuous same characters,
we need to delete all the group but leave only one character.

Explanation
For each group of continuous same characters,
we need cost = sum_cost(group) - max_cost(group)
Hold the character with the biggest cost in hand.

Complexity
Time O(N)
Space O(1)
'''


class Solution:
    def minCost(self, s, cost):
        res = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0
            res += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.minCost(s = "abaac", cost = [1,2,3,4,5]))
