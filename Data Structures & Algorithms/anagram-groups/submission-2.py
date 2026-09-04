from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for word in strs:
            letter_list = [0]*26
            for letter in word:
                letter_list[ord(letter) - ord('a')] += 1
            anagram_dict[tuple(letter_list)].append(word)
        return list(anagram_dict.values())

            