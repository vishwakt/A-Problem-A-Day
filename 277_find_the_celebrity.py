# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:
    return True


class Solution:
    def findCelebrity(self, n: int) -> int:
        # find candidate for celebrity
        # when left and right meet at a point, this person is a potential celebrity
        left, right = 0, n-1
        while left < right:
            if knows(left, right):
                left += 1
            else:
                right -= 1

        # verify if the candidate is a celebrity
        for i in range(n):
            # case 1: at least 1 person doesn't know this candidate => not a celebrity
            if not knows(i, left) and i != left:
                return -1
            # case 2: candidate knows at least one person => not a celebrity
            if knows(left, i) and i != left:
                return -1

        return left
