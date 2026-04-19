class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        # i for what index we are in this string
        for i in range(len(strs[0])):
            for s in strs: 
                
                if i == len(s) or s[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans    