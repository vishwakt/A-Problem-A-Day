from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(0,len(nums)):
            if target-nums[i] in dict:
                return [dict[target-nums[i]], i]
            else:
                dict[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums = [2,7,11,15], target = 9))