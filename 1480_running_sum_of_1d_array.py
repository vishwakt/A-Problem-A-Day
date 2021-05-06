from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumOfList = [0]
        for num in range(0, len(nums)):
            sumOfList.append(sumOfList[num] + nums[num])
        print(sumOfList[1:])
        return sumOfList[1:]


if __name__ == "__main__":
    s = Solution()
    s.runningSum(nums=[1,2,3,4])