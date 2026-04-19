class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        n = len(nums)
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        for num in freq:
            if freq[num] > (n/2):
                return num
