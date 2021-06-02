from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            dfs(i, current, total + candidates[i])
            current.pop()
            dfs(i+1, current, total)

        dfs(0, [], 0)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum(candidates = [2,3,6,7], target = 7))