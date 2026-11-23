class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        count2 = {}

        for elem in s:
            if elem in count:
                count[elem] += 1
            else:
                count[elem] = 1
        for elem2 in t:
            if elem2 in count2:
                count2[elem2] += 1
            else:
                count2[elem2] = 1
        if count == count2:
            return True
        return False
            
        