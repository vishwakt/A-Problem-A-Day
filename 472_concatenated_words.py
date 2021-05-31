from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        words = set(words)

        def DFS(word):
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    return True
                if prefix in words and DFS(suffix):
                    return True

        result = []
        for word in words:
            if DFS(word):
                result.append(word)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.findAllConcatenatedWordsInADict(words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))