class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums[0:k], nums[k:] = nums[len(nums)-k:], nums[0:len(nums)-k]
        return nums


if __name__ == "__main__":
    s = Solution()
    print s.rotate(nums=[1,2,3,4,5,6,7], k=3)