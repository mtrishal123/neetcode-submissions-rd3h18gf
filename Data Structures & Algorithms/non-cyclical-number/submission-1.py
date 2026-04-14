class Solution:
    def isHappy(self, n: int) -> bool:

        c = 0
        check_duplicate = set()
        while True:
            k = n%10
            c += k*k
            n //= 10
            if n < 1:
                if c == 1:
                    return True
                if c in check_duplicate:
                    return False
                check_duplicate.add(c)
                n = c
                c = 0
        return False 