from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:        

        template = Counter(p)

        size_of_window = len(p)

        left_edge, right_edge = 0, size_of_window - 1

        window = Counter(s[:size_of_window])

        res = []
        while right_edge <= len(s) - 1:
            if template == window:
                res.append(left_edge)

            if s[left_edge] in window:
                if window[s[left_edge]] == 1:
                    del window[s[left_edge]]
                else:
                    window[s[left_edge]] -= 1

            left_edge += 1
            try:
                window[s[right_edge + 1]] += 1
            except Exception as e:
                pass
            right_edge += 1

        return res