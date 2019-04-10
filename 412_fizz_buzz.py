class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is 0:
            return []
        list_ = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0:
                list_.append("FizzBuzz")
            elif (i+1) % 3 == 0:
                list_.append("Fizz")
            elif (i + 1) % 5 == 0:
                list_.append("Buzz")
            else:
                list_.append(str(i+1))

        return list_


if __name__ == "__main__":
    s = Solution()
    print s.fizzBuzz(15)