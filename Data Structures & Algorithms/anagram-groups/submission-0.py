class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary in the form {sorted string: array of strings}

        # Iterate through every string in strs
        # Sort the string alphabetically
        # Add to dictionary
        # Return dictionary values

        strs_dict = {}

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s in strs_dict:
                strs_dict[sorted_s].append(s)
            else:
                strs_dict[sorted_s] = [s]
        
        return list(strs_dict.values())
                