class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag1 = {}
        anag2 = {}

        for elem in s:
            if elem in anag1:
                anag1[elem] += 1
            else:
                anag1[elem] = 1
        for elem2 in t:
            if elem2 in anag2:
                anag2[elem2] += 1
            else:
                anag2[elem2] = 1
        if anag1 == anag2:
            return True
        return False