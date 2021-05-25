from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            if i in dict.keys():
                dict[i] += 1
            else:
                dict[i] = 1

        for k, v in dict.items():
            if v == 1:
                return k


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber(nums = [0,1,0,1,0,1,99]))
