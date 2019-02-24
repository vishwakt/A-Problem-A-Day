class BalancedParantheses:
    def __init__(self, data):
        self.data = data
        self.stack = []

    def check_paran(self):
        for i in self.data:
            if i == '(' or i == '[' or i == '{':
                self.stack.append(i)
            else:
                if len(self.stack) is 0:
                    return False
                last = self.stack.pop()
                if not self.parancompare(last, i):
                    return False
        if len(self.stack) is not 0:
            return False
        return True

    def parancompare(self, x, y):
        if x == ')' and y == '(':
            return True
        elif x == ']' and y == '[':
            return True
        elif x == '}' and y == '{':
            return True
        return False


if __name__ == "__main__":
    str_ = BalancedParantheses('{[(()]}')
    if str_.check_paran():
        print "Balanced"
    else:
        print "Not balanced"
