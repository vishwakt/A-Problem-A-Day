class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        answer = ''
        while num > 0:
            for k, v in roman.items():
                if k <= num:
                    answer += v
                    num -= k
                    break
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(3844))