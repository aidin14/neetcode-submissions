class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lett_map = {}
        for word in strs:
            sortedword = "".join(sorted(word))
            if sortedword not in lett_map:
                lett_map[sortedword] = [word]
            else:
                lett_map[sortedword].append(word)
        answer = []
        for word_arr in lett_map:
            answer.append(lett_map[word_arr])
        print(answer)
        return answer