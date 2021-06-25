from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        L, rem = n // 2, n % 2
        if rem != 0:
            ans = [0]
        else:
            ans = []

        for i in range(1, L+1):
            ans.append(-i)
            ans.append(i)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.sumZero(5))
