class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j, k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                two_sum = nums[j] + nums[k]
                if two_sum < target:
                    j += 1
                elif two_sum > target:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return ans