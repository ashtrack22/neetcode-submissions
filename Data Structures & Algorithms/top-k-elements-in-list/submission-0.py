class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]

        for val in nums:
            counter[val] = counter.get(val, 0) + 1
        for val, count in counter.items():
            freq[count].append(val)

        result = []

        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                result.append(val)
                if len(result) == k:
                    return result