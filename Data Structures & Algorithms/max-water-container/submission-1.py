class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                max_area = max(max_area, min(heights[j], heights[i]) * (j - i))
        return max_area