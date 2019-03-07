class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n is 0:
            return [0]

        result = [0]
        for i in range(n):
            result += [x + pow(2, i) for x in reversed(result)]

        return result


if __name__ == "__main__":
    s = Solution()
    print s.grayCode(2)