class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        count = 0

        for spot in flowerbed:
            if spot is 0:
                count += 1
            else:
                count = 0
            if count is 3:
                n -= 1
                count = 1
            if n is 0:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print s.canPlaceFlowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2)
