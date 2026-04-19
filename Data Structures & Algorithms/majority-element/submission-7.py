class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Solution by calculating Frequency and finding the one with majority
        freq = {}
        ans = 0
        maxCount = 0 
        n = len(nums)
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
            if freq[num] > maxCount: 
                maxCount = freq[num]
                ans = num
        return ans
