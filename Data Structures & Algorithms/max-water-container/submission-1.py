class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) -1
        max_area = 0
        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                current_h = heights[left]
                max_area = max(max_area, width * current_h)
                left += 1
            else:
                current_h = heights[right]
                max_area = max(max_area, width * current_h)
                right -=1
        return max_area