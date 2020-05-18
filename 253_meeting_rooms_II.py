from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        print(intervals)
        heap = [] # stores end times
        intervals.sort(key = lambda x: x[0])

        for i in intervals:
            if heap and i[0] >= heap[0]:
                # 2 intervals can use same room
                heapq.heapreplace(heap, i[1])
            else:
                # allocate new room
                heapq.heappush(heap, i[1])

        return len(heap)


if __name__ == "__main__":
    s = Solution()
    print(s.minMeetingRooms(intervals=[[0, 30], [5, 10], [15, 20]]))
