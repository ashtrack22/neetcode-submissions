class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for elem in s:
            if elem in freq1:
                freq1[elem] += 1
            else:
                freq1[elem] = 1
        for elem2 in t:
            if elem2 in freq2:
                freq2[elem2] += 1
            else:
                freq2[elem2] = 1
        if freq1 == freq2:
            return True
        else:
            return False


        