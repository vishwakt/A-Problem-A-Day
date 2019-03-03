from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_counter = Counter(s)

        for i in range(len(s)):
            s_char = s[i]
            print s_char
            if s_counter.get(s_char) == 1:
                return i

        return -1


if __name__ == "__main__":
    s = Solution()
    s.firstUniqChar("leetcode")
