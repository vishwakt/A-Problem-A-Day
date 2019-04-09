class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        if str is "":
            return ""
        x = ""
        for i in str:
            if 64 < ord(i) < 91:
                x += chr(ord(i) + 32)
            else:
                x += i

        return x


if __name__ == "__main__":
    s = Solution()
    s.toLowerCase("")