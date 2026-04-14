class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in arr:
                return [arr[diff], i]
            arr[nums[i]] = i
        return []