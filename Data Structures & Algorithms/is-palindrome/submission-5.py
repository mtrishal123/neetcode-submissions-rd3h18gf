class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        s = s.lower()    
        new_str = ""
        for ch in s:
            if ch.isalnum():
                new_str += ch
        first, last = 0, len(new_str) - 1
        while first < last:
            if new_str[first] == new_str[last]:
                first += 1
                last -= 1
            else:
                return False
        return True