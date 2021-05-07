class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = (0, 1)
        start = [0, 0]
        for instruction in instructions:
            if instruction == 'G':
                start[0] += direction[0]
                start[1] += direction[1]

            elif instruction == 'L':
                direction = (-direction[1], direction[0])
            elif instruction == 'R':
                direction = (direction[1], -direction[0])

        return start == [0, 0] or direction != (0, 1)


if __name__ == "__main__":
    s = Solution()
    print(s.isRobotBounded(instructions="RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"))