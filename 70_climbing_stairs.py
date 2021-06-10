class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = two+one
            two = temp

        return one


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(n=3))