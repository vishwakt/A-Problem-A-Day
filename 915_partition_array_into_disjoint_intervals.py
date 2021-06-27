from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxNow = candidate = nums[0]
        disjoint = 1

        for i in range(1, len(nums)):
            if nums[i] < maxNow:
                disjoint = i + 1
                maxNow = candidate
            else:
                if nums[i] > candidate:
                    candidate = nums[i]

        return disjoint


if __name__ == "__main__":
    s = Solution()
    print(s.partitionDisjoint(nums = [5,0,3,8,6]))