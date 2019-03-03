class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i, key in enumerate(numbers):
            # print i, key
            if target - key in dict:
                return [dict[target - key]+1, i+1]
            dict[key] = i
        # print dict


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([2,7,11,15], 9)