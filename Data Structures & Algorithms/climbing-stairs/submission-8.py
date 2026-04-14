class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)
        memo[1] = 1
        def fib(i):
            if i <= 2:
                return i
            if memo[i]!=-1:
                return memo[i]
            memo[i]=fib(i-1) + fib(i-2)
            return memo[i]
        return fib(n)
