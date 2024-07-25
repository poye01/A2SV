class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_length = min(len(s) for s in strs)
        common_prefix = ""
        for i in range(min_length):
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return common_prefix
            common_prefix += char
        return common_prefix
