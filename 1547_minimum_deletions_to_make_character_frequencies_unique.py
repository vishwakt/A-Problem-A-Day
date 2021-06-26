from collections import Counter


# Collect the frequency of letters in s in a frequency table. Examine the frequencies from highest to lowest. If a
# frequency has been seen, lower it by one by reducing its character. Repeat the operation until all frequencies are
# unique (possibly removing some characters completely).
class Solution:
    def minDeletions(self, s: str) -> int:
        frequencies = Counter(s)

        result = 0

        seen = set()

        for char in frequencies.values():
            while char in seen:
                char -= 1
                result += 1
            if char:
                seen.add(char)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minDeletions(s="aaabbbcc"))
