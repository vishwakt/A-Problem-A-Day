class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        for i in xrange(2, int(n**0.5)+1):
            if primes[i] is not 0:
                primes[i*i:n:i] = [0] * ((n-1-i*i)//i +1)
        return sum(primes)


if __name__ == "__main__":
    s = Solution()
    print s.countPrimes(10)