class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)

        prod = 1

        for i in range(len(nums)):
            output[i] *= prod
            prod *= nums[i]

        prod = 1
        for i in range(len(nums) - 1, -1 , -1):
            output[i] *= prod
            prod *= nums[i]

        return output


if __name__ == "__main__":
    s = Solution()
    print s.productExceptSelf([1,2,3,4])