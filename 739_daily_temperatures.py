from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures(temperatures= [89,62,70,58,47,47,46,76,100,70]))
