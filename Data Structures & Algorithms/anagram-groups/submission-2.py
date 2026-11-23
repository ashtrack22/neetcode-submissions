class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # setting the defualt dict

        for elem in strs: # goes through each string in strs
            count = [0] * 26   # an array to track the count of each alphabet
            for c in elem:
                count[ord(c) - ord("a")] += 1    # sets the count to default indexs, for eg: c - a = 2 which is the placement for 2, this get the count of the char
            
            key = tuple(count)
            result[key].append(elem)
            
        return list(result.values())