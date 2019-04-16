class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        strip_dash = S.replace('-', "").upper()
        lenchars = len(strip_dash)
        if lenchars % K != 0:
            len_first = lenchars % K
        else:
            len_first = K

        res = strip_dash[:len_first] + "-"

        for i in range(len_first, len(strip_dash), K):
            res += strip_dash[i: i + K] + '-'

        return res[:-1]


if __name__ == "__main__":
    s = Solution()
    print s.licenseKeyFormatting("5F3Z-2e-9-wcnjsda7a", 4)