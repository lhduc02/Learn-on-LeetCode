class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        check = 0
        for i in range(min([len(s) for s in strs])):
            check_item = strs[0]
            for value in strs[1:]:
                if check_item[i] != value[i]:
                    return common_prefix
            common_prefix += check_item[i]
        return common_prefix
