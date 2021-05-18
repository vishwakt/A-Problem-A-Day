from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt-coin]+1)

        if dp[amount] != amount+1:
            return dp[amount]
        return -1


if __name__ == "__main__":
    s = Solution()
    s.coinChange(coins = [1,2,5], amount = 11)
