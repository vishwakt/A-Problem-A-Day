from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cache = {}
        totalSum = 0
        for a in nums1:
            for b in nums2:
                if a+b in cache:
                    cache[a+b] += 1
                else:
                    cache[a+b] = 1

        for c in nums3:
            for d in nums4:
                if -(c+d) in cache:
                    totalSum += cache[-(c+d)]
        return totalSum


if __name__ == "__main__":
    s = Solution()