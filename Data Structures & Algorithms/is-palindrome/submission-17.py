import re
class Solution:
    def isPalindrome(self, string: str) -> bool:
        s = re.sub("[:',$@%#$;.!? ]", "", string.lower())
        l,r = 0, len(s) - 1
        for i in range(r):
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
