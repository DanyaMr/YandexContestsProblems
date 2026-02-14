import string

class Solution:
    def isPalindrome(self, s: str) -> bool:

        mask = str.maketrans('','',string.digits + string.punctuation + ' ')
        s = s.translate(mask)

        s = s.lower()


        print(s[::-1])
        print(s)
        if s == s[::-1]:
            return True
        return False
    
if __name__ == "__main__":
    s = Solution()
    s.isPalindrome("A man, a plan, a canal: Panama")
        