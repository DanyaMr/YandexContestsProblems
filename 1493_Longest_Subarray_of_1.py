from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        i, j, = 0, 0
        max_row, current_row = 0, 0
        count_zeros, count_ones = 0, 0

        while j < len(nums):
            if nums[j] == 1:
                count_ones += 1
                current_row += 1

                if current_row > max_row:
                    max_row = current_row
                

            elif nums[j] == 0:
                count_zeros += 1
                if count_zeros > 1:
                    while i < len(nums) - 1 and nums[i] != 0:
                        current_row -= 1
                        i += 1
                    i += 1

            j += 1

        if max_row == len(nums):
            max_row -= 1

        return max_row



if __name__ == "__main__":
    array = [0,1,1,1,0,1,1,0,1]
    sol = Solution()
    print(sol.longestSubarray(array))
    print(sol.longestSubarray([1,1,0,1]))
    print(sol.longestSubarray([1,1,1]))
    print(sol.longestSubarray([1,1,1]))
    print(sol.longestSubarray([1,0,0,0,1]))
    print(sol.longestSubarray([1,1,0,0,1]))
    print(sol.longestSubarray([1,1,1,1,0,1,0,1,1]))

        
        