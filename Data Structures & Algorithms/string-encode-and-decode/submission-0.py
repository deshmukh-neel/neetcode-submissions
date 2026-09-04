class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        if not strs:
            return encoded_string 
        for s in strs:
            encoded_string += (str(len(s)) + "#" + s)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        char = 0
        res = []
        while char < len(s):
            delimiter = char
            num_string = ""
            while s[delimiter] != "#":
                delimiter += 1
            string_length = int(s[char: delimiter])
            word_start = delimiter + 1
            word_end = word_start + string_length
            res.append(s[word_start:word_end])
            char = word_end
        return res
        
        