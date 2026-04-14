class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         hash_set = set(nums)
         if(len(nums) == len(hash_set)):
            return False
         return True