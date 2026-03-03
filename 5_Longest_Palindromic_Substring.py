class Solution:
    def longestPalindrome(self, s: str) -> str:

        t = "#" + "#".join(s) + "#"

        n = len(t)
        p = [0] * n
        c = 0
        r  = 0

        for i in range(n):

            if i < r:
                p[i] = min(r - i, p[2 * c - i])

            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            
            if i + p[i] > r:
                c = i
                r = i + p[i]

        max_len = max(p)
        center_index = p.index(max_len)
        
        start = (center_index - max_len) // 2
        
        return s[start : start + max_len]