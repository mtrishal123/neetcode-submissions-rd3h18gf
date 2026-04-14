class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mapper:
                return [mapper[diff], i]
            mapper[nums[i]] = i
        return []