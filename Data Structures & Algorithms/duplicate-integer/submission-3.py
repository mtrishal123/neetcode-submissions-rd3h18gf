class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        num_len = len(nums)
        n = len(set(nums))
        if(num_len == n):
            return False
        return True