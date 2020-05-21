from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        print(intervals)
        res = []
        intervals.sort(key=lambda x: x[0])

        for i in intervals:
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge(intervals=[[1,3],[2,6],[8,10],[15,18]]))
