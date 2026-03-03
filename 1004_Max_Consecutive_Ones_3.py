from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left, right = 0, 0
        max_val = 0
        count_zeros = 0
        cur_val = 0
        while right < len(nums):


            if nums[right] == 0:
                if count_zeros == k:
                    while nums[left] != 0:
                        left += 1
                        cur_val -= 1
                    left += 1
                else:
                    count_zeros += 1
                
            else:
                cur_val += 1

            right += 1

            max_val = max(cur_val, max_val)

        if max_val + k < len(nums):
            return max_val + k
        else:
            return len(nums)