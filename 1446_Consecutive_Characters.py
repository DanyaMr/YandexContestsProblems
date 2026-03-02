class Solution:
    def maxPower(self, s: str) -> int:

        cur_char = None
        count = 0
        max_count = 0
        for i in s:
            if cur_char != i:
                cur_char = i
                count = 1
            else:
                count += 1
            max_count = max(max_count, count)

        
        return max_count
            