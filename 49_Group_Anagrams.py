from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            d[tuple(count)].append(s)
            
        return list(d.values())


if __name__ == "__main__":
    sol =Solution()
    sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
