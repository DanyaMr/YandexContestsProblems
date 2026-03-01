from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        
        left_prefix_max, right_prefix_max = [0] * n, [0] * n

        max_left = 0
        for i in range(n):
            if height[i] > max_left:
                max_left = height[i]

            left_prefix_max[i] = max_left

        max_right = 0
        for i in range(n - 1, -1, -1):
            if height[i] > max_right:
                max_right = height[i]

            right_prefix_max[i] = max_right

        sum_ = 0
        for i in range(n):
            sum_ += min(left_prefix_max[i], right_prefix_max[i]) - height[i]
        
        return sum_