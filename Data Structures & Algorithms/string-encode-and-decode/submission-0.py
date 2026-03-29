class Solution:

    def encode(self, strs: List[str]) -> str:
        # Encoded format: "<numberofstrings>:<str1len>:<str2len>:str3len>:<...>:concatination of all strings"
        encoded_message = ""
        encoded_message += str(len(strs)) + ":"

        for s in strs:
            encoded_message += str(len(s)) + ":"

        for s in strs:
            encoded_message += s
        
        return encoded_message

    def decode(self, s: str) -> List[str]:
        # Get number of strings
        i = 0
        while s[i] != ":":
            i += 1
        number_of_strings = int(s[0:i])
 
        # Get string lengths
        lengths = []

        i += 1
        starting_index = i

        while len(lengths) < number_of_strings:
            if s[i] == ":":
                lengths.append(int(s[starting_index:i]))
                starting_index = i + 1
            i += 1
        
        #loop through lengths and add to list of strs
        strs = []

        for l in lengths:
            strs.append(s[starting_index:starting_index + l])
            starting_index = starting_index + l

        return strs

            




        
