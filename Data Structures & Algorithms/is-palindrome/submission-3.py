import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        if(len(s) <= 1):
            return True
        s = s.lower().replace(" ","").strip()
        if(s[-1] == '?' or s[-1] == '.' or s[-1] == '!'):
            s = s[:-1]
        rev = ""
        for i in range(len(s)-1,-1,-1):
            rev = rev+s[i]
        print(rev)
        if(rev == s):
            return True
        return False
