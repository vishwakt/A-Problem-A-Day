class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"]": "[", "}": "{", ")": "("}
        stack_ = []
        for bracket in s:
            if bracket in dict.values():
                stack_.append(bracket)
            elif bracket in dict.keys():
                if stack_ == [] or dict[bracket] != stack_.pop():
                    return False
            else:
                return False
        return stack_ == []


if __name__ == "__main__":
    s = Solution()
    print s.isValid("()")