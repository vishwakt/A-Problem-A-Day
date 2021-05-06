class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[0 for i in range(len(word2)+1)] for x in range(len(word1)+1)]
        for i in range(len(word2)):
            dp[0][i+1] = i+1
        for j in range(len(word1)):
            dp[j+1][0] = j+1
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.minDistance(word1 = "intention", word2 = "execution"))