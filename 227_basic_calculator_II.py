class Solution:
    def calculate(self, s):
        num, stack, sign = 0, [], '+'
        for index in range(len(s)):
            if s[index].isdigit():
                num = num * 10 + int(s[index])
            if s[index] in "+-*/" or index == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = s[index]
        return sum(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.calculate(s = "3+2*2"))