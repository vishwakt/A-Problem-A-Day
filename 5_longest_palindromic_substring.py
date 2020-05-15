class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenOfString = len(s)
        answer = ''
        maxLength = 0
        DP = [[0]*lenOfString for _ in range(lenOfString)]

        for i in range(lenOfString):
            DP[i][i] = True
            maxLength = 1
            answer = s[i]

        for i in range(lenOfString-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                maxLength = 2
                answer = s[i:i+2]

        for j in range(lenOfString):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if maxLength < j - i +1:
                        maxLength = j - i + 1
                        answer = s[i:j+1]

        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome(s="babad"))
