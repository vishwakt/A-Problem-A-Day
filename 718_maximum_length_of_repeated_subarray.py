from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums2) + 1)] for x in range(len(nums1) + 1)]
        maxCount = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1]+1
                    maxCount = max(maxCount, dp[i][j])
        return maxCount


if __name__ == "__main__":
    s = Solution()
    print(s.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))


