class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        hashset = set()

        left, count = 0, 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[r])
            count = max(count, r - left + 1)
        return count