class NGE:
    def __init__(self, arr):
        self.arr = arr

    def print_nge(self):
        stack = []
        for x in range(len(self.arr), 0, -1):
            while len(stack) > 0 and stack[-1] < self.arr[x-1]:
                stack.pop()
            if len(stack) is 0:
                print self.arr[x-1], -1
            else:
                element = stack.pop()
                print self.arr[x-1], element
                stack.append(element)
            stack.append(self.arr[x-1])


if __name__ == "__main__":
    x = [4, 5, 2, 25]
    nge = NGE(x)
    nge.print_nge()