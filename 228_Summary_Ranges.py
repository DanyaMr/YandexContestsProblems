class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        ans = []
        j = 0
        b = nums[0]
        for i in nums:
            if j < len(nums) and  not b == nums[len(nums) - 1]:
                a = nums[j]
            else:
                break 

            while j < len(nums) - 1:
                if nums[j + 1] == nums[j] + 1:
                    b = nums[j + 1]
                else:
                    if a >= b:
                        ans.append(str(a))
                    elif a != b:
                        ans.append(str(a) + "->" + str(b))
                    else:
                        ans.append(str(b))
                    
                    j += 1
                    break
                j += 1  

        if a >=b:
            ans.append(str(a))
        elif a != b:
            ans.append(str(a) + "->" + str(b))
        return ans

def main():
    sol = Solution()
    # nums = [0,2,4,6,8,10]
    # print(sol.summaryRanges(nums))
    # nums = [0,2,3,4,6,8,9]
    # print(sol.summaryRanges(nums))
    
    nums = []
    print(sol.summaryRanges(nums))
    nums = [1,3]
    print(sol.summaryRanges(nums))
    nums = [0]
    print(sol.summaryRanges(nums))
    nums = [0,2,3,4,6,8,9]
    print(sol.summaryRanges(nums))
    nums = [0,1,2,4,5,7]
    print(sol.summaryRanges(nums))

if __name__ == "__main__":
    main()