from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0

        L = len(beginWord)

        comboDict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                comboDict[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while queue:
            curWord, level = queue.popleft()
            for i in range(L):
                intermediateWord = curWord[:i] + "*" + curWord[i+1:]
                for word in comboDict[intermediateWord]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))