class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solution 1, sorting O(m*nlogn) 
        # Where mm is the number of strings and n is the length of the longest string. 
        # lett_map = defaultdict(list)
        # for word in strs:
        #     sortedword = "".join(sorted(word))
        #     lett_map[sortedword].append(word)
        # answer = []
        # for word_arr in lett_map:
        #     answer.append(lett_map[word_arr])
        # print(answer)
        # return answer

        # Solution 2: O(m*n) Where mm is the number of strings and nn is the length of the longest string. 
        answer = defaultdict(list)
        for s in strs:
            #array with alphabet representation
            count = [0] *26 
            for c in s:
                count[ord(c)-ord("a")]+=1
            answer[tuple(count)].append(s)
        return list(answer.values())