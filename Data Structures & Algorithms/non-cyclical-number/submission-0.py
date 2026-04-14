class Solution:
    def isHappy(self, n: int) -> bool:
        s = 0
        m = n
        arr = set()
        while(True):
            j = n%10
            s += j*j
            n //= 10
            if (n < 1):
                if(s == 1):
                    return True
                if(s in arr):
                    return False
                arr.add(s)
                n = s
                s = 0
        return True
            