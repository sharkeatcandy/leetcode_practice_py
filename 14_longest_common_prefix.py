# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in strs:
            while not i.startswith(common_prefix):
                common_prefix = common_prefix[:-1]
                print(common_prefix)
                if common_prefix == "":
                    return common_prefix
        return common_prefix
