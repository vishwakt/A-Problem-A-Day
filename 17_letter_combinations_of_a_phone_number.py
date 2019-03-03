from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or len(digits) is 0:
            return []
        results = ['']
        dict_of_numbers = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for digit in digits:
            results = [result + d for result in results for d in dict_of_numbers[digit]]
        return results


if __name__ == "__main__":
    s = Solution()
    print s.letterCombinations('234')
