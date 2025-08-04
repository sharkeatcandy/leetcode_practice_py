# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        temp_str = ""
        len_needle = len(needle)
        len_haystack = len(haystack)
        for i in range(len_haystack):
            temp_str += haystack[i]
            if len(temp_str) % len_needle == 0:
                if temp_str == needle:
                    return i + 1 - len_needle
                else:
                    temp_str = temp_str[1:]
        return -1
