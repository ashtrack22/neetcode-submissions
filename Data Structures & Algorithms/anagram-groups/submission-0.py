class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for word in strs:
            signature = "".join(sorted(word))

            if signature not in dict1:
                dict1[signature] = []
            dict1[signature].append(word)
        return list(dict1.values())