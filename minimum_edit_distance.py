class Solution(object):
    def editDistance(self, str1, str2, m, n):
        """
        :type str1: str
        :type str2: str
        :type m: int
        :type n: int
        :rtype: str
        """

        # If first string is empty, then insert all characters of second string to the first
        if m == 0:
            return n

        if n == 0:
            return m

        # If last characters of the 2 strings are same, then ignore the characters and get the count for the remaining
        if str1[m-1] == str2[n-1]:
            return self.editDistance(str1, str2, m-1, n-1)

        return 1 + min(self.editDistance(str1, str2, m, n-1),
                       self.editDistance(str1, str2, m-1, n),
                       self.editDistance(str1, str2, m-1, n-1))


if __name__ == "__main__":
    s = Solution()
    str1 = "sunday"
    str2 = "saturday"
    print (s.editDistance(str1, str2, len(str1), len(str2)))