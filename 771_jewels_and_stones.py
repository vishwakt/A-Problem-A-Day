class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if J is None:
            return 0
        if S is None:
            return 0
        dict_jewels = {}
        count = 0

        for jewel in J:
            dict_jewels[jewel] = 1

        for stone in S:
            if stone in dict_jewels:
                count += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print s.numJewelsInStones(J = "z", S = "ZZ")
