class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        c = 0
        a, b = 1, 2
        for i in range(1, n - 1):
            c = a + b
            a = b
            b = c
        return c