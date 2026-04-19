class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for elem in nums:
            freq[elem]=1+freq.get(elem,0)
        arr = []
        for num,frq in freq.items():
            arr.append([frq,num])
        arr.sort()
        ans = []
        for r in range(k):
            ans.append(arr.pop()[1])
        return ans