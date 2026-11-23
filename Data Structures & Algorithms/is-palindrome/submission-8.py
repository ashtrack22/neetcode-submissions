class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        s = s.lower()
        
        while l < r:
            if s[l].isalnum() == False:
                l += 1
            if s[r].isalnum() == False:
                r -= 1
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]:
                    return False
                elif s[l] == s[r]:
                    r -= 1
                    l += 1
        return True
