class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_consecutive = 0

        unique_nums = set(nums)

        while unique_nums:
            consecutive = 1

            current_number = unique_nums.pop()

            next_number = current_number + 1
            while next_number in unique_nums:
                unique_nums.remove(next_number)
                consecutive += 1
                next_number += 1

            prev_number = current_number - 1
            while prev_number in unique_nums:
                unique_nums.remove(prev_number)
                consecutive += 1
                prev_number -= 1

            longest_consecutive = max(longest_consecutive, consecutive)

        return longest_consecutive


if __name__ == "__main__":
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2, 5])