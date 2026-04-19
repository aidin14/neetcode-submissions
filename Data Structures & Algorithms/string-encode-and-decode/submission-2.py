class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        for s in strs:
            enc_str += s
            enc_str += 'π'
        return enc_str
    def decode(self, s: str) -> List[str]:
        ans = []
        curr_word = ''
        for letter in s:
            print(letter)
            if letter == 'π':
                ans.append(curr_word)
                curr_word = ''
            else: 
                curr_word += letter
        print(ans)
        return ans