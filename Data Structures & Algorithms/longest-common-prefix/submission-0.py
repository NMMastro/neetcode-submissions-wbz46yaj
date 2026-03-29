class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:

            if len(prefix) > len(s):
                prefix = prefix[0:len(s)]

            for ind in range(len(prefix)):
                if s[ind] != prefix[ind]:
                    prefix = prefix[0:ind]
                    break

        return prefix