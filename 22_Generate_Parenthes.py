from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def inner(current_str, opened, closed):
            
            
            if opened + closed == n * 2:
                res.append(current_str)
                return
            

            if opened < n:
                inner(current_str + "(", opened + 1, closed)
        
            if opened > closed:
                inner(current_str + ")", opened, closed + 1)

        inner("", 0, 0)  


        return res