class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        leftPtr = 0
        longestSubStr = 0

        for rightPtr in range(len(s)):
            while s[rightPtr] in charSet:
                charSet.remove(s[leftPtr])
                leftPtr += 1
            charSet.add(s[rightPtr])
            longestSubStr = max(longestSubStr, rightPtr - leftPtr + 1)

        return longestSubStr


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))