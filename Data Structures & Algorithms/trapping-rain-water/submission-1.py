class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0

        for i in range(len(height)):
            prefix = suffix = height[i]
            for j in range(i):
                prefix = max(prefix, height[j])
            for j in range(i + 1, len(height)):
                suffix = max(suffix, height[j])
            
            max_water += min(prefix, suffix) - height[i]
        
        return max_water