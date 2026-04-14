class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        res = 0
        for num in nums:
            curr, streak = num, 0
            while curr in store:
                curr += 1
                streak += 1
            res = max(streak, res)
        return res