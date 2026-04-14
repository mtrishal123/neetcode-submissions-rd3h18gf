class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicate_set = set()
        for i in nums:
            if i in check_duplicate_set:
                return True
            check_duplicate_set.add(i)
        return False
        