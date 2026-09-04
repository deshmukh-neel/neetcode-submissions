class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        list_dict = defaultdict(list)
        for word in strs:
            letter_list = [0] * 26
            for letter in word:
                letter_list[ord(letter) - ord('a')] += 1
            list_dict[tuple(letter_list)].append(word)
        return list(list_dict.values())