class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            l = r = i
            result += self.getPali(s, l, r)
            l = i
            r = i + 1
            result += self.getPali(s, l, r)
        return result

    def getPali(self, s, l, r):
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            result += 1
            l -= 1
            r += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings(s="aaa"))
