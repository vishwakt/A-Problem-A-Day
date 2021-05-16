class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"]": "[", "}": "{", ")": "("}
        stack = []

        for bracket in s:
            if bracket in dict.values():
                stack.append(bracket)
            elif bracket in dict.keys():
                if stack == [] or dict[bracket] != stack.pop():
                    return False
            else:
                return False

        return stack == []


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("([)]"))