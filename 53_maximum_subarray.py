class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            # print i, nums[i-1]
            if nums[i-1] > 0:
                # print nums[i]
                nums[i] += nums[i-1]
                # print nums[i], '\n'
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])