from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count_non_zero = 0
        
        for num in nums:
            if num != 0:
                nums[count_non_zero] = num
                count_non_zero += 1

        for i in range(count_non_zero, len(nums)):
            nums[i] = 0

        print(nums)

if __name__ == "__main__":
    sol = Solution()
    sol.moveZeroes([0,1,0,3,12])