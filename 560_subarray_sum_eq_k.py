from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0

        sums_dict = {0: 1}
        
        for num in nums:
            current_sum += num
            
            if (current_sum - k) in sums_dict:
                count += sums_dict[current_sum - k]
            
            sums_dict[current_sum] = sums_dict.get(current_sum, 0) + 1
            
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1,1,1], 2))
    print(sol.subarraySum([1,2,3], 3))
    print(sol.subarraySum([1], 0))

