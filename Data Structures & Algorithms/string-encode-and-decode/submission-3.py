class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        for s in strs:
            enc_str += str(len(s))
            enc_str += '#'
            enc_str += s
        print(enc_str)    
        return enc_str
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            count = int(s[i:j])
            ans.append(s[j+1:j+1+count])
            i = j+1+count
            
        print(ans)
        return ans