class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [[-1] * (n + 1) for _ in range(n)]
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if cache[i][prev + 1] != -1:
                return cache[i][prev + 1]
            LIS = dfs(i + 1, prev)

            if prev == -1 or nums[prev] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))
            cache[i][prev + 1] = LIS

            return LIS
        return dfs(0, -1)